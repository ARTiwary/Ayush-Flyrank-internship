# Build Log & MVP Execution Report: Groq-Powered Portfolio Assistant (FL-07)

## 1. Overview & Core Job

* **Assignment Code:** FL-07
* **Track:** General AI Fluency (Week 5)
* **Core Job:** Build and execute an MVP version of the Groq-powered portfolio assistant that connects to a real local data source, completes an end-to-end user request without mid-run intervention, and logs the development iteration.

---

## 2. Build Log: Iteration, Failures, & Scope Cuts

| Phase                | What Broke / Obstacle                                                                                              | What Was Changed / Fixed                                                                                                                                   | What Was Cut & Why                                                                               |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Initial Setup**    | Groq API rate limits were triggered when attempting large batch scans of the entire GitHub repository history.     | Restricted the data source context to active root Markdown files and key project configuration metadata.                                                   | Cut historical commit scanning to stay within efficient token limits and the 10-hour MVP scope.  |
| **Tool Integration** | The custom `fetch_repo_contents` script failed to correctly parse nested file paths during local testing.          | Switched to a direct local workspace file parser combined with the Groq client endpoint (`llama-3.3-70b-specdec`).                                         | Cut automated remote GitHub webhook triggers and used a local script execution loop for the MVP. |
| **Prompt Alignment** | The model initially hallucinated extra technologies, such as React Native, that were not present in the portfolio. | Strengthened system instructions with strict grounding constraints: "Never fabricate project features or tech stacks not explicitly present in the files." | Cut general conversational fluff to prioritize accurate, grounded answers.                       |

---

## 3. End-to-End Execution Flow (MVP Proof)

1. **User Request:**
   "List the primary technologies used in Ayush's portfolio based on the active local workspace files."

2. **Tool Execution:**
   The assistant reads the relevant local workspace files, including `README.md` and project specifications.

3. **Groq Inference:**
   The retrieved file context is passed to Groq using the `llama-3.3-70b-specdec` model.

4. **Final Result:**
   The assistant returns a clean, accurate, non-hallucinated breakdown of the technologies based on the available project files, without manual text editing during the run.

---

## 4. Screen Capture Link

**Raw Run Recording (approx. 2 minutes):**

[▶️ **Watch / Play the Screen Recording**](./Screen%20Recording.mp4)

The `Screen Recording.mp4` file is stored in the same repository folder as this `README.md`.

### Repository Structure

```text
3 Build the Agent/
├── README.md
└── Screen Recording.mp4
```

---

## 5. FL-07 Evaluation Criteria

* **End-to-end execution:** Completed successfully without mid-run hand-editing.
* **Real data connection:** Uses the local workspace files as the data source.
* **FL-06 alignment:** Portfolio assistant concept maintained; deviations are documented above.
* **Build iteration:** Failures, fixes, and scope cuts are documented in the build log.
* **Raw run capture:** Approximately 2-minute unedited screen recording is included in the repository.

---

## 6. Status

**FL-07 MVP completed.**
