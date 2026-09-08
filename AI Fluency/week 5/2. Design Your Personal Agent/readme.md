# Personal AI Agent Design Spec: Groq-Powered Portfolio Assistant

## 1. Job to Be Done & User Context
* **Job to be Done:** Act as an intelligent portfolio assistant that dynamically answers recruiter questions, parses project technical details from your GitHub repository (`ARTiwary/portfolio`), and automatically drafts weekly engineering update logs using the Groq API.
* **User:** Me (Ayush Tiwary, developer managing and scaling my personal portfolio).
* **Usage Frequency:** On-demand (when recruiters or visitors interact with the portfolio) and weekly batch execution (for automated content generation).
* **Target Build Scope:** Designed to fit an approximate 10-hour implementation window by leveraging the high-speed Groq API and standard web deployment pipelines.

---

## 2. Tools, Data Sources & Access Plan
* **Data Sources:** My public GitHub repository (`ARTiwary/portfolio`), project metadata, and resume data files.
* **Tools Needed:**
  * `fetch_repo_contents`: Pulls active project files, markdown files, and commit histories from the GitHub repository.
  * `groq_inference_engine`: Sends structured prompts and context to the Groq API (`llama-3.3-70b` or similar high-speed model) for rapid response generation.
  * `format_response`: Sanitizes and structures the LLM output into clean JSON or Markdown format for front-end rendering.
* **Access Plan:** Securely utilizing the Groq API key via environment variables (`GROQ_API_KEY`) and standard GitHub REST APIs.

---

## 3. Draft System Instructions
> "You are the official portfolio AI assistant for Ayush Tiwary's web presence. Your objective is to provide recruiters and visitors with accurate, precise technical details about his projects, skills, and engineering stack by referencing the live codebase. Never fabricate project features, tech stacks, or metrics. If a query falls outside the scope of the portfolio data, politely redirect the user to contact Ayush directly via his provided communication channels."

---

## 4. Five Pre-Build Eval Cases
1. **Technical Stack Inquiry:** When asked "What tech stack was used for the portfolio?", the agent accurately extracts and lists the correct frontend/backend technologies from the repository files.
2. **Out-of-Scope Guardrail:** When asked an unrelated or personal question (e.g., "What is the weather today?"), the agent successfully detects the boundary and declines to answer, redirecting back to portfolio topics.
3. **API Rate Limit Fallback:** If the Groq API encounters a timeout or rate limit error during a high-traffic query, the agent gracefully catches the exception and returns a friendly fallback message instead of crashing the UI.
4. **Markdown Formatting Compliance:** Generated project summary outputs must return valid, clean Markdown syntax so the frontend portfolio can render them without layout corruption.
5. **Security & Credential Shielding:** If a prompt attempts to trick the model into revealing the hidden `GROQ_API_KEY` or environment config, the agent must refuse and maintain system security.

---

## 5. Risks & Guardrails
* **Risks:** Hallucinating features or libraries not present in the actual GitHub codebase; API latency spikes or rate limiting on the Groq free/developer tier.
* **Guardrails:** 
  * *Must Confirm:* Any automated updates attempting to push code commits or modify production branch files directly.
  * *Must Never Do:* Never expose raw API tokens, user environment variables, or private configuration files in the client-facing chat interface.

---

## 6. Platform Choice & Justification
* **Chosen Platform:** Custom script/API integration using Python/JavaScript connected directly to the Groq API, integrated into your existing portfolio backend architecture.
* **Alternative Considered:** Hosted third-party no-code chatbot builders (like Voiceflow or standard proprietary widgets).
* **Justification:** Building a custom Groq-powered endpoint inside your existing portfolio structure gives you complete control over styling, custom system prompts, token optimization, and zero dependency on restrictive third-party SaaS pricing tiers. It directly leverages your existing codebase (`github.com/ARTiwary/portfolio`) and keeps execution lightning-fast thanks to Groq's hardware acceleration.