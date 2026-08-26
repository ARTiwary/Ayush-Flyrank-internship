# Workflows, Agents, and MCP — and What FL-04 Would Need to Become an Agent

## Workflow vs. agent, in plain terms

A **workflow** is a system where a human has already decided the steps, and code just calls the LLM at each fixed point. The path through the system is written in advance: step 1 always leads to step 2, which always leads to step 3. The LLM does the *thinking inside* each step, but it never decides *what step comes next* — that's hardcoded.

An **agent** is a system where the LLM itself decides what to do next, in a loop, based on what actually happens in the environment. It looks at a result (a tool call, a search, a piece of code running), decides whether that's enough, and chooses its own next action — call another tool, ask the human, or stop. Nobody wrote down in advance how many steps it will take or which tools it will use in which order.

The distinction isn't about how "smart" or autonomous the system feels — it's architectural. Who controls the sequence: the code, or the model?

## FL-04 classification: workflow, not agent

My FL-04 pipeline ("Draft, Critique, Revise") is a **workflow**, specifically a **prompt chain**. The stages are fixed in a system prompt: Draft → Critique → Revise/Polish, always in that order, always three passes. The Claude Project follows the instructions I wrote; it doesn't decide whether to skip the critique stage, run it twice, or call in an outside source if the draft looks thin. NotebookLM feeds a digest in at the start, and a human reviews at the end — but nothing in the middle is deciding its own path. Even the "Devil's Advocate" persona is just another fixed step, not the model choosing to critique.

This matters because the pipeline works well *because* it's a workflow — it's predictable, cheap, and I can audit each handoff. An agent version would cost more (more tokens, more turns) for a task that doesn't need open-ended judgment about *what* to do next, only better judgment *within* each fixed step.

## What MCP is, and its three primitives

MCP (Model Context Protocol) is the standard way to plug external systems into an LLM application without writing a custom integration for every tool. Anthropic describes it as a USB-C port for AI apps — one connector shape, many devices. Instead of hardcoding "call the Gmail API this way, call the Notion API that way," an app just speaks MCP, and any MCP server (Gmail, filesystem, GitHub, whatever) exposes itself the same way.

MCP defines three primitives a server can expose:

1. **Tools** — actions the model can invoke (send an email, run a query, create a file). These are the things that actually do something in the world.
2. **Resources** — data the app can read and hand to the model as context (a file's contents, a database row, a webpage). These are read-only, model doesn't call them like functions — the client fetches them.
3. **Prompts** — pre-written prompt templates the server offers, so a common task (e.g., "summarize this ticket") doesn't need to be reinvented by every client.

The distinction that matters for the agent-vs-workflow question: tools are what give an LLM the ability to *act* in a loop against a live environment, rather than just talk about it.

## Connecting an MCP server and what it unlocked

I connected [NAME THE SERVER YOU ACTUALLY USE — filesystem / GitHub / etc.] as an MCP server in [Claude Desktop / Claude.ai connector / whichever client]. Three tasks I ran through it that plain chat could not do:

1. [Task 1 — e.g., "list and read the actual files in my FL-04 folder" — chat alone can't see my filesystem, this required a real tool call.]
2. [Task 2 — e.g., "pull the latest commit history from the repo" — requires live GitHub API access, not something the model can know from training.]
3. [Task 3 — e.g., "check today's date/weather/a live API value" — anything that changes after training cutoff and isn't searchable text.]

Screenshots of each tool call are attached, showing the request going out and a real result coming back — not the model guessing or hallucinating an answer.

## What FL-04 would need to become an agent

Right now FL-04 has no tools and no feedback loop — it's three prompts run in sequence with a human checking the output at the end. To become an agent, the single most concrete upgrade would be:

**Give the Critique stage a real tool to verify claims, and let the model decide when to stop revising.** Concretely: connect an MCP server that can search the web or query NotebookLM's sources directly, and instead of Stage 2 producing a static critique from memory, have it actually check the "claims that require precise source verification" it flags. Then loop Draft → Critique → Revise until the critique stage reports zero unresolved fact or logic flags (with a max-iteration cap), rather than always running exactly one revision pass. That single change — a tool call plus a model-decided stopping condition — is what would turn this from a fixed three-step chain into a genuine agent.

*(~830 words)*