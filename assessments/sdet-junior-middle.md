# SDET (Junior-Middle) – Take-Home Assessment

## Overview
Design and implement automated tests for the JSONPlaceholder API, a free fake REST API for testing and prototyping.
This assessment evaluates your approach to API testing, including test planning, automation, and code organization.

## System under test
- JSONPlaceholder API: `https://jsonplaceholder.typicode.com/`
- Key endpoints to focus on:
  - `GET /posts` - Retrieve all posts
  - `GET /posts/{id}` - Retrieve a specific post
  - `POST /posts` - Create a new post
  - `PUT /posts/{id}` - Update a post
  - `DELETE /posts/{id}` - Delete a post

## Assumptions
- No authentication is required for this API
- The API returns simulated responses (data isn't actually persisted)
- HTTP status codes and response formats follow REST conventions

## Deliverables (ZIP or GitHub link)

1. **Test Plan Outline** (Markdown or PDF) – **bullet points only**:
   - Scope & API endpoints to test
   - Test-Case Table (4-5 scenarios covering different HTTP methods)
   - Key validations to perform (status codes, response format, etc.)

2. **Automation Suite** in your preferred language (Java, Python, JavaScript):
   - Code to automate at least three API test scenarios
   - Must include at least one POST/PUT request with request body validation

3. **README** with:
   - Setup instructions
   - How to run the tests
   - Dependencies required

4. **AI Disclosure** – list any AI tools (ChatGPT, Claude, etc.) you used

## Evaluation Criteria
- Test coverage and scenario selection
- Code organization and readability
- Assertions and validations
- Error handling
- Documentation quality

---

**Good luck!** We'll review your work and discuss your approach during the interview.
