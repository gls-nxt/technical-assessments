# QA Engineer - Take-Home Test

## Overview

You will verify key aspects of the live GLS parcel-shipping flow by defining test cases and delivering an automated suite. Total effort: ~2–3 hours.

---

## Deliverables (ZIP or GitHub link)

- **Test Plan Outline** (Markdown or PDF), including:
  - **Scope & Flows Under Test**
  - **Structured Test-Case Table** (happy and negative paths)
  - **Smoke Checklist** (5 items)
- **Automation Suite** (source files) in your preferred language/framework (Kotlin, Java, or TypeScript recommended)
  - Identify and automate at least two critical scenarios of your choosing
  - Include a README with instructions to install dependencies and execute tests (e.g., `./gradlew test`, `mvn test`, or `npm test`)

---

## Scope & Flows Under Test

**Base URLs (production):**

- **Parcel Configuration:**
  - `https://www.gls-pakete.de/en/private-customers/parcel-shipping/parcel-configuration`
- **Cart:**
  - Reached by clicking "Add to shopping cart"
- **Checkout:**
  - `https://www.gls-pakete.de/en/private-customers/parcel-shipping/checkout`

### Assumptions

- This is live production—any "Buy now" will redirect to a real gateway (do not complete payment)
- Use valid-format but fake data (e.g., "4111 1111 1111 1111") to trigger validation
- No login required

### 1. Flows to Cover (candidate defines critical pieces)

**Parcel Configuration → Cart:**
- Select a parcel size
- Enter dimensions/weight
- Fill sender & recipient addresses
- Choose service options
- Click **Add to shopping cart**
- Verify Cart contents and **To check out** navigation

**Checkout → Payment Gateway Redirect:**
- On Checkout, fill Sender fields (First Name *, Last Name *, Street *, House Number *, Postal Code *, City *, Email *)
- Optionally apply a discount code
- Select payment method (Card or PayPal)
- Click **Buy now**
- Confirm redirection (PayPal site or card validation)

---

## 2. Test-Case Table (candidate to create)

Provide a table of at least six scenarios (three "happy" and three "negative"):

| Title | Preconditions | Steps (automatable) | Expected Result |
|-------|---------------|---------------------|-----------------|
| ...   | ...           | ...                 | ...             |

*Candidates should fill in actual titles, steps, and expected results*

---

## 3. Smoke Checklist (5 Items)

List five core checks your suite (or manual sanity run) would cover, for example:

- Parcel Configuration page loads correctly
- Required-field validation appears when "Weight" is blank
- ...

---

## 4. Automation Requirements (≈1.5 hr)

- **Language/Framework:** Choose any (preferably Kotlin, Java, or TypeScript) with Playwright, Selenium, Cypress, or similar
- **README / Instructions:**
  - List prerequisites (e.g., JDK, Node.js)
  - Provide setup commands (`./gradlew build`, `npm install`)
  - Provide test execution commands (`./gradlew test`, `npx playwright test`)

---

## Evaluation Criteria

- **Clarity & Organization:** Well-structured plan and code
- **Coverage & Depth:** Relevant positive/negative paths automated
- **Maintainability:** Modular page objects or helper functions
- **Reliability:** Tests pass consistently without flakiness
- **Pragmatism:** Scoped to ~2–3 hours, focusing on high-value checks

---

Good luck! We look forward to reviewing your submission.

Would you like me to generate the qa-engineer.md file for you now and match the filename and style of your other files exactly (I see you already uploaded qa-engineer.md — I can overwrite or update it as needed)? Just confirm and I'll prepare it! 🚀