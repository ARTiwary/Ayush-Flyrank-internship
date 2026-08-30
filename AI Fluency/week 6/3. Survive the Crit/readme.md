# Survive the Crit — Design Review & Fix Log

**Student Name:** Ayush Raj Tiwary
**Track / Phase:** General AI Fluency • Week 6: Survive the Crit (Build+ Phase)

**Live Portfolio:** https://artiwary.netlify.app/
**GitHub Repository:** https://github.com/ARTiwary/portfolio

## 1. Proof Statement & Reviewer Questions

To initiate the design critique, I provided my reviewer, a fellow developer and peer, with my live portfolio URL and the following official **Proof Statement** to judge the portfolio against its actual job:

> *“An AI/ML Engineer and Full-Stack Developer who designs and builds production-grade intelligent systems—demonstrated by deploying 94% accurate computer vision models with real-time gesture control, Groq-powered multilingual RAG applications, and interactive full-stack architectures.”*

### Initial Reviewer Setup Questions

1. **In ten seconds, what do I do?**
2. **Would you believe I'm good at it based on what you see?**

## 2. Raw Reviewer Feedback Log

* **Feedback Item A:** “The initial hero text introduces you as a developer, but the very first screen requires scrolling down a bit to see any concrete proof of your AI/ML projects. Make the primary value proposition tighter right at the top.”

* **Feedback Item B:** “The live demo link for the Smart Dining Assistant works well, but the text styling on mobile for the subtitle description has slightly low contrast against the dark background.”

* **Feedback Item C:** “Your projects are strong, but the GitHub repo link for the MRI tumor detection project was slightly buried below the tech stack badges, making it a bit hard to spot at a glance.”

* **Feedback Item D (Nice-to-Have):** “Add a small filter toggle at the top of the projects section so visitors can sort between Full-Stack vs. AI/ML projects instantly.”

## 3. Must-Fix vs. Nice-to-Have Sort

| **Feedback Category** | **Item Description**                               | **Action Plan**                                                                                                          |
| --------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Must-Fix**          | Hero text & value proposition clarity (Feedback A) | Refine the top-level hero copy so visitors instantly recognize the AI/ML + Full-Stack focus within the first 10 seconds. |
| **Must-Fix**          | Mobile subtitle contrast adjustment (Feedback B)   | Update text color variables on secondary descriptions to fully pass contrast ratios on mobile screens.                   |
| **Must-Fix**          | Project repository link visibility (Feedback C)    | Move and restyle the GitHub and Live Demo action buttons to a prominent, consistent position on every project card.      |
| **Nice-to-Have**      | Project filtering toggle (Feedback D)              | Defer to a future enhancement sprint after core functionality and mobile layout stability are locked.                    |

## 4. Evidence of Must-Fixes Addressed on the Live Site

Following the critique, I executed code updates on the live repository and pushed the fixes directly to production:

* **Hero Value Proposition Updated:** Rewrote the hero introductory header and sub-headline to immediately display the core title, **AI/ML Engineer & Full-Stack Developer**, along with high-impact metrics within the initial viewport.

* **Contrast Fixes Applied:** Adjusted text color contrast variables on card descriptions to improve readability and accessibility across mobile viewports.

* **Button Layout Standardization:** Restructured the action button grid inside every project card. GitHub repository links and live deployment buttons are now explicitly grouped side-by-side with distinct hover states and expanded touch targets.

## 5. Outcome

The critique resulted in three targeted production fixes focused on the portfolio’s most important first-impression issues:

1. The AI/ML + Full-Stack positioning is now immediately visible.
2. Secondary project text has improved readability on mobile devices.
3. Project GitHub and Live Demo actions are easier to discover and use.

The project filtering toggle was intentionally deferred because it is a **nice-to-have enhancement**, while the three identified usability and communication issues were prioritized as **must-fix** items.

Overall, the review helped turn subjective feedback into concrete implementation changes and provided a clear record of the design decisions, priorities, and fixes made during the **Survive the Crit** phase.
