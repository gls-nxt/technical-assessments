# Technical Assessment – Senior Product Security Engineer (Device & Cloud)

## Overview
This challenge assesses your ability to design and reason about the **security of smart connected devices** that interact with cloud services.
The exercise focuses on applying **security-by-design principles**, identifying threats, and demonstrating **practical mitigations** across device, network, and cloud layers.

You can use any format you prefer (Markdown, PDF, or text) for your submission.

---

## Scenario
Your company develops a line of **smart connected devices** deployed globally.  
Each device runs a small **edge computing node** (based on Linux) that:
- Exposes a local **user interface** (e.g., touchscreen or web interface)
- Connects to sensors and actuators (for example, temperature sensors, relays, or payment terminals)
- Communicates with a **cloud platform** via MQTT and HTTPS APIs
- Receives **over-the-air (OTA)** updates using a container-based update mechanism

You’ve been asked to **design and evaluate the security posture** of this system.

---

## Part 1 – Threat Modeling (written design)
Using STRIDE or a similar methodology, outline the **top security risks** for:
1. The **edge device** (physical and software threats)
2. The **communication channel** (device ↔ cloud)
3. The **backend/cloud infrastructure** (API, authentication, update delivery)

For each threat, describe:
- The **attack scenario**
- The **impact** (confidentiality, integrity, availability)
- The **mitigation strategy** you’d apply

Deliverable: a short written table or list summarizing your threat model.

---

## Part 2 – Secure Architecture Proposal
Design a **secure end-to-end architecture** diagram or description that covers:
- **Device identity and provisioning** (how devices are securely onboarded)
- **Mutual authentication** between device and cloud (e.g., mTLS, PKI)
- **Update security** (integrity validation, rollback protection)
- **Secrets management** (how credentials are stored and rotated on-device)
- **Monitoring & logging** (how anomalies or breaches are detected and reported)

You can describe this textually or include a simple diagram.

---

## Part 3 – Security Governance & Compliance
Write a short section (~1 page) describing:
- How you would ensure **“security by design”** within the engineering organization
- Which **IoT security standards or frameworks** you would align to (e.g., ETSI EN 303 645, NISTIR 8259A, OWASP IoT Top 10)
- Your approach for **vulnerability disclosure, patch management**, and **incident response**

---

## Submission
Please submit:
- A short document or `README.md` covering your architecture, threat model, and governance answers.

Expected effort: **4-6 hours** total.  
We’re not looking for production-ready solutions - we’re looking for your **thought process and security design reasoning**.

---

## Bonus Discussion Topics (for follow-up interview)
- Device identity rotation and decommissioning.
- Secure remote logging and telemetry privacy.
- Designing for compliance with **EU Cyber Resilience Act** and **UK PSTI**.
- Hardware Root of Trust integration (TPM, secure enclave).

---

**Good luck — we look forward to seeing how you approach securing our next-generation smart connected devices!**
