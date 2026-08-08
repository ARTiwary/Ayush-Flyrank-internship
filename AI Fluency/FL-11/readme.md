# Three Roads: Choose Your Stack — Reasoning

**Constraints:** The AI was offered free hosting only. I am a hybrid developer, with primary emphasis on fullstack (MERN) and additional interest in GenAI/ML. The portfolio at [artiwary.netlify.app](https://artiwary.netlify.app) should feature a scroll-triggered parallax hero, a projects section with hover-over links to GitHub and/or live demo, an About section, and a contact form which emails me directly. Image galleries, embedded demos, or lengthy articles are disfavored — it is a link-out portfolio. The only truly dynamic element is the contact form.

## Three options considered

1. **Static site + Netlify Forms** — write the page in HTML/CSS/JS and host it on Netlify, which will handle form submissions directly. This is the easiest option, requiring no backend at all, but it does little to showcase my backend skills.

2. **React + EmailJS** — write the site in React (with scroll animations done via Framer Motion or GSAP), and send contact form submissions to EmailJS, a third-party email service, via their JS API. Again, nothing is hosted on my backend, though this hides the implementation detail better.

3. **React + Express (Nodemailer, Render)** — write the site in React and host it on Netlify, then use Express.js (Nodemailer) and Render to process contact form submissions via a custom API route. This option truly demonstrates backend skills, but it requires me to host and maintain a server.

## Final choice

**Option 3** — React frontend + Netlify, Express backend + Render/Nodemailer for the contact form.

**Reasons for this choice:** I want to transition into the GenAI space, and having a live backend on my portfolio is an opportunity to demonstrate my fullstack abilities, which I am not currently fully showcasing. The first two options fail to demonstrate any backend skills whatsoever, and the third one, while not using my own backend, hides the lack thereof behind the third-party service.

**Am I likely to keep developing and maintaining it?** Yes — while Render's free tier is not meant for production use and will shut down inactive servers, the downtime between consecutive contact form submissions can be reasonably mitigated by client-side "Sending…" UI and/or a cron job which sends a test request to the backend to keep it awake. It is a fairly simple app with a narrow purpose — there isn't much that can go wrong.

**Do I think this is an adequate showcase of my skills?** Partly, but not fully, since most of the site is static and a potential employer would not be able to tell the difference between options 1 and 3 without testing the contact form. However, I believe my ability to implement a backend is evident from the existence of the project pages: my linked GitHub repos include a FastAPI/Python app with a CNN model as well as a MERN project, both of which demonstrate my ability to design and implement a functional backend from scratch, as opposed to using a CMS or a third-party service like Firebase.