## Senior Frontend Engineer Technical Assessment: Build a Reusable Toast Notification System

### Overview

This assessment evaluates your skills as a Senior Frontend Engineer through the implementation of a real-world UI component: a toast notification system. You must build this using React and its ecosystem (e.g., build tools, styling libraries), and clearly justify any additional choices. You will design and build a flexible, accessible React-based toast library that showcases component composition, theming, animations, and testing.

---

### Scenario

Your application needs a lightweight, standardized toast notification system for user feedback (success, error, info, warning). Notifications should stack, auto-dismiss, and allow manual dismissal. Consumers must be able to customize appearance and behavior.

---

### Tasks

#### 1. Core Functionality

* **Objective**: Implement a basic notification mechanism that allows developers to display transient messages to users.
* **Scope**: Decide how notifications are created, displayed, and dismissed, and how they integrate into an application’s component hierarchy.

#### 2. Theming & Customization

* **Objective**: Provide a mechanism for developers to adapt the look and feel of their notifications to fit different application styles and branding.

#### 3. Animation & Performance

* **Objective**: Provide smooth entry/exit animations without jank and demonstrate consideration of performance budgets.

  * Use CSS transitions or a lightweight animation library.
  * Ensure toasts don’t cause layout shifts.
  * Optimize rendering so adding/removing toasts doesn’t re-render the entire list unnecessarily.
  * Define and adhere to basic performance metrics or budgets (e.g., maximum animation duration, layout shift score) and illustrate how you would measure these (e.g., browser devtools, performance APIs).

#### 4. Accessibility

* **Objective**: Ensure the system is usable for all users by considering screen-reader announcements, focus behavior, and control accessibility.

#### 5. Testing & Quality Assurance

* **Objective**: Provide a robust test suite.

  * Unit tests for hook behaviors (triggering, stacking, auto-dismiss).
  * End-to-end tests simulating user triggers and dismissals.

---

### Deliverables

1. **Code Repository**: Provide a public GitHub repository link containing the complete project—source code, setup instructions, and documentation. If a public repo isn’t feasible, include a downloadable `.zip` with the same contents.

2. **README File**: At the root of your repository (or included in the `.zip`), provide a `README.md` that includes:

   * **Overview & Design Rationale**: Explain your component API, key architecture decisions, and trade‑offs.
   * **Setup Instructions**: How to install dependencies, run the development server, build for production, and execute tests.
   * **Usage Examples**: Code snippets showing how to trigger notifications and configure options.
   * **Theming & Customization**: Guidance on overriding styles, positioning, and theming approaches.
   * **Accessibility Notes**: Summary of how accessibility concerns are addressed.
   * **Performance Metrics**: Any performance budgets or measurements collected (e.g., animation durations, layout shift scores).
   * **Testing Instructions**: Commands to run unit and end‑to‑end tests and view coverage reports.

3. **Hosted Demo (Optional)**: A live deployment (e.g., Vercel/Netlify) showcasing the toast system in action; desirable but not mandatory.

---

## Submission Guidelines

- **Deadline**:
    - As provided in the E-Mail.

- **Submission Method**:
    - Please send your completed assessment to: [glsnxt-engineering-leads@teams.gls-global.com](mailto:glsnxt-engineering-leads@teams.gls-global.com).

---

## Final Notes

There is no single “correct” solution to this assessment. This is intended to understand your approach to solving the problem. We value clarity, justification of choices, and adherence to best practices. Focus on detailing your thought process and explaining trade-offs if any. 

Good luck, and we look forward to reviewing your solution!
