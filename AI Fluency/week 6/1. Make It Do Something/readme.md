# General AI Fluency: Assignment Submission
**Week 6 Track:** Make It Do Something  
**Student Name:** Ayush Raj Tiwary  
**Live Portfolio:** https://artiwary.netlify.app/  
 

---

## 1. The Live Dynamic Feature & Evidence

For this assignment, I wired a fully functioning backend-powered **Contact Form** directly into my React + Vite portfolio (https://artiwary.netlify.app/). Rather than just rendering static HTML text, the form captures visitor inquiries securely, triggers backend server processing, routes the transmission directly to my inbox (`ayushrajtiwary07@gmail.com`), and sends an automated acknowledgement back confirming receipt.

**Verification & Evidence:** Multiple test submissions have been executed on the live production URL. The payloads successfully bypass client-side validation, transit through the server backend infrastructure, and land in my personal email client in real time.

---

## 2. Plain-Words Explainer (Backend & Data Flow)

**What a backend is:**  
A backend is the hidden server-side infrastructure that handles data processing, executes requests, and manages communication behind the scenes of a web application. While the frontend (built with React and Vite) controls the visual presentation, styling, and animations that users directly experience in their browser, the backend acts as the secure processing engine that accepts incoming submissions, filters them, and routes them to the correct destinations.

**What my feature does:**  
The dynamic feature integrated into my portfolio is a fully functional contact form. Instead of serving as static elements on a screen, it allows visitors, recruiters, and prospective collaborators to input their names, email addresses, and messages directly into the site and transmit them instantly without forcing them to manually open an external email client or mail application.

**How the data flows:**
1. **User Input:** A visitor enters their name, email address, and message into the contact form input fields on my live portfolio website (`https://artiwary.netlify.app/`) and triggers the submit button.
2. **Client-Side Network Request:** The browser packages these input parameters into an HTTP network request and securely transmits the data payload away from the static frontend hosting environment directly to the configured backend form-handler service endpoint.
3. **Backend Processing & Routing:** The backend infrastructure intercepts the incoming data payload, validates the form fields, executes security and spam checks, and formats the raw text variables into a clean notification layout.
4. **Final Delivery & Response:** The backend processes the message and pushes an email notification directly to my personal inbox (`ayushrajtiwary07@gmail.com`), allowing me to view and reply directly to the sender while simultaneously returning a confirmation response to the user interface.