**Note (Draft for Interview Preparation)**  
> This take-home is a sketch to prepare for our discussion—you don’t need to send polished prose or full explanations. Please share bullet-point outlines, minimal code files, and any AI tools you used; we’ll dive into details live during the interview.

# QA Engineer – Take-Home Test (2–3 Hours)

## Overview  
Define your approach and automate key flows of the live GLS parcel-shipping journey. Treat your submission as an outline and code “sketch” – detailed reasoning will happen in our interview.

## System under test:
- Parcel Configuration:  
  `https://www.gls-pakete.de/en/private-customers/parcel-shipping/parcel-configuration`  
- Cart: reached by clicking **Add to shopping cart**  
- Checkout:  
  `https://www.gls-pakete.de/en/private-customers/parcel-shipping/checkout`
  
## Assumptions
- This is live production—any "Buy now" will redirect to a real gateway (do not complete payment)
- Use valid-format but fake data (e.g., "4111 1111 1111 1111") to trigger validation
- No login required

## Deliverables (ZIP or GitHub link)

1. **Test Plan Outline** (Markdown or PDF) – **bullet points only**, no long essays:  
   - Scope & Flows Under Test  
   - Test-Case Table (up to six scenarios: 3 happy, 3 negative)  
   - Smoke Checklist (5 core checks)  
2. **Automation Suite** (source files) in your preferred framework/language (Kotlin, Java, or TypeScript):  
   - Code to automate at least two scenarios you choose
3. **README** – brief setup & run commands  
4. **AI Disclosure** – list any AI tools (ChatGPT, Copilot, etc.) you used

## Evaluation Criteria

- Clarity & Organization
- Coverage & Depth
- Maintainability
- Reliability
- Pragmatism

---

**Good luck!** We’ll review your outline & code, then dig deeper together in the interview
