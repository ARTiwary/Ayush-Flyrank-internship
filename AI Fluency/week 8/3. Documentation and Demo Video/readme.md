# GTA x Apple Glassmorphism Portfolio & AI Agent (`artiwary.netlify.app`)

An ultra-responsive, high-performance personal portfolio and interactive AI agent blending Apple's sleek glassmorphism design language with a vibrant Grand Theft Auto (GTA) cinematic aesthetic.

Built for recruiters, universities, and technical reviewers to immediately experience full-stack projects and interactively query developer background data through **Ayush Orbit**.

---

## What It Does & For Whom

* **For Recruiters & Hiring Managers:** Provides immediate access to resume downloads, live project links, GitHub repositories, and direct technical breakdowns through a built-in multilingual conversational agent.
* **For Reviewers & Peers:** Showcases end-to-end full-stack capabilities, computer vision models, and generative AI architectures through a seamless, high-performance web interface.

---

## Setup & Local Reproduction

To run this portfolio locally:

```bash
# Clone the repository
git clone https://github.com/ARTiwary/portfolio.git

# Navigate into the project directory
cd portfolio

# Install dependencies
npm install

# Run the development server
npm run dev
```

Open the following URL in your browser:

```text
http://localhost:3000
```

---

## Usage Examples

### Browsing Projects

Scroll through interactive project cards showcasing work such as:

* **NeuroCore** — Brain Tumor Detection
* **Smart Dining Assistant**
* **Gesture File Transfer**

Each project provides a concise overview of its purpose, technical implementation, and relevant resources.

### Interacting with the AI Agent

Click the floating **Ayush Orbit** chat widget to query:

* Technical skills
* Educational background
* Technology stacks
* Project architecture
* AI/ML experience
* Individual project details
* Direct project URLs

The agent provides an interactive way for recruiters and reviewers to explore the portfolio beyond static project cards.

---

## Architecture Sketch

```text
[ User / Browser ]
       │
       ▼
[ Netlify Edge / CDN ]
       │
       ▼
[ Frontend: React / Next.js + Tailwind CSS ]
       │
       ├──► [ Apple Glassmorphism + GTA Cinematic UI ]
       │
       ├──► [ Static Assets / Resume PDF ]
       │
       └──► [ Ayush Orbit AI Agent / LLM Integration ]
                    │
                    ▼
             [ External APIs / RAG Backend ]
```

---

## v2 Evaluation Results

### Performance

Achieves sub-second initial load times with high optimization scores across local testing environments and production deployments on Netlify.

Performance considerations include optimized assets, efficient component rendering, responsive layouts, and controlled use of visual effects.

### Responsiveness

The interface has been validated across multiple device and viewport sizes, with attention to:

* Responsive layouts
* Smooth UI transitions
* Glassmorphism rendering
* CSS animation performance
* Mobile usability
* Visual consistency

---

## Limitations

The portfolio intentionally uses complex CSS `backdrop-filter` effects and cinematic background layers to create its visual identity.

On certain lower-end mobile GPUs, these effects can occasionally introduce minor rendering, compositing, or scrolling overhead.

Potential future improvements include:

* Reducing backdrop-filter usage on lower-powered devices.
* Optimizing cinematic background assets.
* Introducing adaptive visual effects based on device capabilities.
* Further minimizing unnecessary animation and rendering work.

---

## AI Transparency Note

Built with AI collaboration using advanced LLMs to assist with architectural scaffolding, component patterns, code optimization, debugging, and copy refinement.

AI was used as a development and thinking partner rather than as an unchecked code generator. All core architectural decisions, personal phrasing, visual styling choices, implementation decisions, and final code reviews were personally evaluated and hand-validated.

---

## Demo Video Submission Link

* **Live Walkthrough Video (3–5 min end-to-end run):** (https://www.youtube.com/watch?v=5nab_N2ETWA)

The walkthrough will demonstrate:

1. Landing page and visual design.
2. Responsive navigation and portfolio sections.
3. Project cards and individual project information.
4. Resume and external project links.
5. Interaction with the **Ayush Orbit** AI agent.
6. Example technical queries and responses.
7. Overall end-to-end user experience.
