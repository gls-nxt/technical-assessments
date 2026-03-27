import asyncio
import random
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException

app = FastAPI(title="Mock Upstream Service")

SHIPMENTS = {
    f"shp-{i:03d}": {
        "shipmentId": f"shp-{i:03d}",
        "recipientCountry": random.choice(["DE", "NL", "FR", "PL", "IT", "ES"]),
        "createdAt": (datetime(2026, 3, 20, tzinfo=timezone.utc) + timedelta(hours=i)).isoformat().replace("+00:00", "Z"),
        "promisedDeliveryDate": f"2026-03-{25 + (i % 5):02d}",
    }
    for i in range(1, 201)
}

STATUS_FLOW = ["PICKED_UP", "IN_TRANSIT", "OUT_FOR_DELIVERY", "DELIVERED"]
HUBS = ["DEHAM01", "DEBER01", "NLAMS01", "FRPAR01", "PLWAW01", "ITMIL01"]

class GeneratorState:
    def __init__(self):
        self.next_id = 1
        self.shipment_steps = {shipment_id: 0 for shipment_id in SHIPMENTS.keys()}
        self.last_event_by_shipment = {}
        self.duplicate_probability = 0.15
        # Prefer active shipments so delivered shipments do not dominate the stream.
        self.active_shipment_pick_probability = 0.9
        # How likely each lifecycle step is to advance after an event is emitted.
        # Lower probability at IN_TRANSIT keeps more shipments in that status.
        self.advance_probability_by_step = {
            0: 0.7,  # PICKED_UP -> IN_TRANSIT
            1: 0.2,  # IN_TRANSIT -> OUT_FOR_DELIVERY
            2: 0.5,  # OUT_FOR_DELIVERY -> DELIVERED
        }

    def _pick_shipment_id(self):
        active_shipments = [
            shipment_id
            for shipment_id, step in self.shipment_steps.items()
            if step < len(STATUS_FLOW) - 1
        ]
        # When all shipments have been delivered, cycle them back to the start.
        if not active_shipments:
            self.shipment_steps = {shipment_id: 0 for shipment_id in SHIPMENTS.keys()}
            self.last_event_by_shipment = {}
            active_shipments = list(SHIPMENTS.keys())
        if random.random() < self.active_shipment_pick_probability:
            return random.choice(active_shipments)
        return random.choice(list(SHIPMENTS.keys()))

    def make_event(self):
        shipment_id = self._pick_shipment_id()

        last_event = self.last_event_by_shipment.get(shipment_id)

        # Duplicate existing event with same eventId
        if last_event is not None and random.random() < self.duplicate_probability:
            return last_event

        # After DELIVERED, this shipment can only emit exact duplicates.
        if last_event is not None and last_event.get("status") == "DELIVERED":
            return last_event

        shipment_step = self.shipment_steps[shipment_id]
        if shipment_step >= len(STATUS_FLOW):
            shipment_step = len(STATUS_FLOW) - 1

        # Before DELIVERED: generate forward progress only.
        status = STATUS_FLOW[shipment_step]
        event_time = datetime.now(timezone.utc)

        event = {
            "eventId": f"evt-{self.next_id:06d}",
            "shipmentId": shipment_id,
            "status": status,
            "timestamp": event_time.isoformat().replace("+00:00", "Z"),
            "hubCode": random.choice(HUBS),
        }
        self.next_id += 1

        # Before DELIVERED, advance probabilistically to keep more IN_TRANSIT traffic.
        current_step = self.shipment_steps[shipment_id]
        if current_step < len(STATUS_FLOW) - 1:
            should_advance = random.random() < self.advance_probability_by_step.get(current_step, 0.5)
            if should_advance:
                self.shipment_steps[shipment_id] += 1

        self.last_event_by_shipment[shipment_id] = event
        return event

state = GeneratorState()

@app.get("/external/shipments/{shipment_id}")
async def get_shipment(shipment_id: str):
    shipment = SHIPMENTS.get(shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    await asyncio.sleep(0.05)
    return shipment

@app.get("/health")
async def health():
    return {"status": "UP"}

@app.websocket("/tracking")
async def tracking(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await websocket.send_json(state.make_event())
            await asyncio.sleep(0.2)
    except WebSocketDisconnect:
        return
