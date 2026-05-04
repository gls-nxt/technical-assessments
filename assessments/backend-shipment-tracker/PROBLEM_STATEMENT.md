# Shipment Tracking Aggregator – Starter Package

You are building a **Shipment Tracking Aggregator Service**.

The service consumes tracking events, enriches them with shipment metadata, and exposes read APIs for clients.

## What we provide

- `starter-app/` — a Spring Boot + Kotlin starter application
- `mock-upstream/` — a mock upstream service

Start the mock upstream:

```bash
docker compose up --build
```

This exposes:

- WebSocket stream: `ws://localhost:8081/tracking`
- Metadata API: `GET http://localhost:8081/external/shipments/{shipmentId}`

The starter app already connects to both on startup. Run it from `starter-app/`:

```bash
./gradlew bootRun
```

The app starts on port `8080`.

## Your task

Build a working shipment-tracking backend using the provided upstream interfaces.

Expose these APIs:

- `GET /shipments?status=IN_TRANSIT`
- `GET /shipments/{shipmentId}`
- `GET /shipments/{shipmentId}/events`

## API expectations

- `GET /shipments?status=IN_TRANSIT` returns shipments currently in the given status.
- `GET /shipments/{shipmentId}` returns the current aggregated state for a single shipment.
- `GET /shipments/{shipmentId}/events` returns event history for that shipment.

## Constraints

- Use **in-memory storage only** for this take-home (no database required in this phase).
- Implement this as a **single service** and do not introduce additional infrastructure components.
- In your README, briefly explain how you would evolve this to durable storage in a next phase.

## Submission expectations

Please include:

- runnable code
- tests for key behaviors
- a short README section explaining:
  - how to run
  - assumptions
  - key design decisions
  - known limitations and next improvements
