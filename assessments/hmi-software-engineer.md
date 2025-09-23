# Technical Assessment – HMI Software Engineer (IoT Devices)

## Overview
As part of our hiring process, we’d like you to complete a short technical challenge.  
The goal is to demonstrate your ability to design and implement an **interactive kiosk-style application** using **Qt (QML + C++)**.  

The exercise is designed to be completed in about **3–5 hours**. Please don’t over-engineer - we value clarity, resilience, and usability over feature completeness.

---

## Challenge: Parcel Locker Mini-Kiosk

### Goal
Build a simple interactive application that simulates a **parcel pickup flow** for a smart locker. The app should run on **macOS** and showcase fundamentals of GUI development, state management, and hardware/backend integration in Qt.

---

## Features

Your application should include the following screens:

1. **Welcome**  
   - Fullscreen display with a “Start” button.  
   - Show network status (online/offline).

2. **Code Entry**  
   - Numeric keypad and masked input field.  
   - Buttons: “Back” and “Confirm”.

3. **Validating**  
   - Loading animation/spinner.  
   - Simulate async call to a mock backend.

4. **Door Control**  
   - Show locker door status.  
   - Buttons: “Open Door”, “Close Door”.

5. **Result**  
   - Display **success** (green) or **error** (red) with a message.  
   - Automatically return to the Welcome screen after a short delay.

---

## Behaviors

- **State Machine**: Use QML `States`/`Transitions` or C++ `QStateMachine` to drive navigation.  
- **Mock Backend**:  
  - On “Confirm”, check against `mock_api.json`.  
  - If valid → success with locker details.  
  - If invalid → error message.  
- **Mock Device (Door)**:  
  - Implement a `DoorController` class in C++.  
  - Expose `open()`, `close()`, `statusChanged` to QML.  
  - Simulate success/failure with random delays or error rates.  
- **Offline Mode**:  
  - Simulate “offline” state (toggle with a hidden gesture/menu).  
  - In offline mode, backend calls should fail fast with clear UI.  
- **Kiosk UX**:  
  - Large tap targets.  
  - ESC exits in desktop mode.  
  - Handle edge cases (empty input, retries, timeouts).  

---

## Non-Functional Requirements
- Use Qt 6.x, QML for UI, C++ for backend/device mocks.
- Provide a CMake-based build.
- Include a README.md with setup instructions for macOS (brew/Qt install, build/run steps).
- Include 1–2 simple QTest unit tests (e.g., door controller retry logic, code validation).

---

## Acceptance Criteria
- Runs on macOS; operable with mouse (fullscreen optional with `--fullscreen`)
- Happy path: Welcome → Code Entry → Validating → Door Control → Result → back to Welcome
- Error handling for invalid codes, offline mode, and simulated door failures
- Async handling (no frozen UI)
- Clear code organization (UI vs. logic separation)
- Documentation (README) and at least minimal testing

---

## Stretch Goals (Optional)
- If you have extra time:
  - Add localization (e.g., English/Portuguese toggle)
  - Implement simple theming (light/dark)
  - Add telemetry logging (local file: screen transitions, errors)

---

## What to Submit
- GitHub repo or zipped project folder
- Short note (in README) describing design choices and tradeoffs
- (Optional) A short screen recording or GIF of the app flow

---

## Mock Data

Example `data/mock_api.json`:

```json
{
  "codes": [
    {"pin": "123456", "lockerId": "A-12", "items": ["BOX-001"]},
    {"pin": "777777", "lockerId": "B-03", "items": ["ENV-544"]}
  ]
}
