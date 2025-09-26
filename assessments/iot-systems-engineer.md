# Technical Assessment – Senior IoT Systems Engineer (Edge & IoT)

## Overview
As part of our hiring process, we’d like you to complete a practical challenge focused on **edge computing, IoT messaging, and containerized deployment**.  
The scenario mirrors our core domain: **a smart parcel locker fleet** that exchanges events and commands with the cloud.  

This exercise is designed to be completed in **3–6 hours**. Please prioritize **clarity, resilience, and clean design** over feature completeness.

---

## Challenge: Parcel Locker Edge Service

### Goal
Build an **edge service** in **Go** that manages locker events and communicates with a mock cloud service via **MQTT**.  
The service should be **containerized with Docker** and runnable locally.

---

## Requirements

### Core Features
1. **Locker Event Simulation**  
   - Simulate locker hardware by generating events (e.g., `door_opened`, `door_closed`, `health_check`).  
   - Events should include metadata: `lockerId`, `timestamp`, `status`.

2. **MQTT Publisher/Subscriber**  
   - Publish locker events to an MQTT topic (e.g., `lockers/{lockerId}/events`).  
   - Subscribe to a command topic (e.g., `lockers/{lockerId}/commands`) to receive instructions such as `open_door` or `restart`.  
   - Acknowledge commands with a response event (e.g., `lockers/{lockerId}/ack`).

3. **Configurable Locker Service**  
   - Locker ID, MQTT broker URL, and other settings should be configurable via **environment variables** or a simple config file.

4. **Dockerized Deployment**  
   - Provide a `Dockerfile` to build and run the service.  
   - Container should be configurable at runtime with environment variables.

5. **Resilience**  
   - Handle MQTT connection loss gracefully (retry, backoff).  
   - Ensure the service can run unattended for long periods.

---

## Bonus (Optional)
- Add **persistent state** (e.g., log events to a local SQLite file or JSON log).  
- Provide a **health check HTTP endpoint** (e.g., `/healthz`) to expose service status.  
- Add a **unit test** for MQTT message handling or command parsing.  
- Multi-container `docker-compose.yml` including a local MQTT broker (e.g., Eclipse Mosquitto).

---

## Non-Functional Requirements
- **Language**: Go (1.20+)  
- **Dependencies**: Use widely adopted Go MQTT client libraries (e.g., Eclipse Paho, EMQX client).  
- **Containerization**: `Dockerfile` with clear build/run instructions.  
- **Documentation**: `README.md` with steps to build, run, and test.  
- **Code Organization**: Separation of concerns (e.g., `mqtt/`, `simulator/`, `cmd/locker-service/`).

---

## Acceptance Criteria
- Service builds and runs locally (bare metal or Docker).  
- Locker events are published to MQTT broker topics.  
- Service reacts to incoming MQTT commands and responds appropriately.  
- Configurable via environment variables.  
- Clean, readable Go code with proper error handling.  

---

## What to Submit
- GitHub repo or zipped project folder.  
- `README.md` with build/run instructions (bare metal + Docker).  
- Notes on design choices and any tradeoffs made.  

---

Good luck — we’re excited to see your work!
