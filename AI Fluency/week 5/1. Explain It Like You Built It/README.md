# Explain It Like You Built It: Understanding the Model Context Protocol (MCP)

If you're talking to a friend who has never built a site or set up AI tools before, the easiest way to explain what I built here is to think of it like giving a smart assistant a secure key to open a specific drawer on my computer.

Normally, when you talk to an AI like ChatGPT or Claude, it lives inside its own digital bubble. It can write code or give you advice, but it can't actually see your local folders, open your real project files, or save things directly onto your hard drive. 

To bridge that gap, I used something called the **Model Context Protocol (MCP)**. 

Think of MCP as a universal translator or a secure standard plug-in. It consists of two main parts:
* **The Client (The Brain/Interface):** In my test, this was the local MCP Inspector dashboard running in my web browser, which acts as the control center talking to the protocol.
* **The Server (The Hands/Tool):** This is a small, secure microservice—specifically, the secure filesystem server—that I locked down so it only has permission to look at one single folder on my computer (`FL-14`).

Instead of writing custom, messy code to connect an AI model to my local files, MCP standardizes how they communicate. The server exposes specific "tools" like `list_directory`, `read_file`, and `write_file`. When the inspector calls those tools, the server safely executes them inside my folder, reads my actual files, and even writes a brand-new audit log file (`mcp_audit_log.md`) right onto my workspace—all while keeping everything secure because it is blocked from touching anything outside that designated folder.

In short, I built and tested a live local pipeline where an AI architecture can securely reach out of its digital bubble and interact directly with a real local file system.