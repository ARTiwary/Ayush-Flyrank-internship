# Personal Website & Hosting Infrastructure

## Project Overview

This project is my personal portfolio website, created to present my professional profile, technical skills, projects, and contact information in one public place.

The website is deployed on Netlify and is publicly accessible over HTTPS.

**Live Portfolio:** https://artiwary.netlify.app/

**Author / Owner:** Ayush Raj Tiwary

**Program:** FlyRank Internship Program — General AI Fluency

**Assignment:** PF-04 — Personal Website Live on the FlyRank Domain

---

## Purpose of the Website

The website is designed to serve as a central professional profile where visitors can learn about my background, technical capabilities, projects, and ways to contact me.

The main sections include:

* **Hero / Positioning:** Introduces me as an AI/ML Engineer and Full-Stack Developer.
* **About Me:** Provides information about my academic background and professional interests.
* **Projects / Works:** Presents selected AI, machine learning, and full-stack projects.
* **Technical Skills:** Covers areas such as Generative AI, RAG, vector databases, LLM systems, full-stack development, databases, and DevOps.
* **AI Assistant — Ayush Orbit:** An interactive assistant that provides information about my skills, projects, and background.
* **Resume / CV:** Provides access to my professional resume.
* **Contact:** Provides ways for visitors to contact me and access my professional profiles.
* **Future Work:** Provides a foundation for adding future projects, posts, and capstone work.

---

## Technical Stack and Hosting

### Frontend

The portfolio uses modern web technologies including:

* React
* JavaScript / JSX
* HTML5
* CSS3
* Responsive UI components
* Custom styling and interactive components

### Hosting

The website is hosted on **Netlify** using its free hosting infrastructure.

Netlify provides:

* Public hosting
* HTTPS
* SSL/TLS certificate provisioning
* Global content delivery
* Deployment of the built website

The live website is:

**https://artiwary.netlify.app/**

The website uses the free `netlify.app` subdomain, so purchasing or configuring a separate custom domain was not required for this assignment.

---

## Main Portfolio Projects

The portfolio presents several technical projects, including:

### NeuroCore

A computer-vision-based brain tumor detection interface incorporating AI-based image analysis and gesture-control interaction.

### Smart Dining Assistant

A full-stack intelligent application that uses language-model capabilities to assist users with dining-related tasks.

### Suraksha-Setu

An AI-driven safety-oriented system designed around intelligent assistance and safety protocols.

### Road Accident Detection System

An AI-based system focused on detecting road accidents and supporting automated safety responses.

These projects demonstrate experience across artificial intelligence, computer vision, full-stack development, and intelligent application design.

---

# DNS Walkthrough

## What is DNS?

DNS stands for **Domain Name System**. It translates human-readable domain names into information that computers can use to locate the requested service.

For example, a person can type:

`artiwary.netlify.app`

instead of having to remember a numerical IP address.

DNS works like a distributed directory for the Internet. It allows users to use domain names while the underlying network infrastructure uses IP addresses and other DNS information.

---

## What happens when someone visits the website?

When someone enters `artiwary.netlify.app` into a browser, several steps happen before the website is displayed.

### 1. The browser and local system check for cached information

The browser and operating system may already have DNS information stored in their caches.

If the required information is available, the system may be able to avoid performing the complete DNS lookup again.

If it is not available, the computer sends a DNS query to a **recursive DNS resolver**.

---

### 2. The recursive resolver searches for the answer

A recursive resolver is a DNS service that finds the required DNS information on behalf of the user's computer.

The resolver may already have the answer in its cache.

If it does not, it follows the DNS hierarchy to find the appropriate information.

The hierarchy includes:

1. **Root DNS servers**
2. **Top-Level Domain (TLD) DNS servers**
3. **Authoritative DNS servers**

For this website, the domain uses the `.netlify.app` namespace.

The resolver follows the appropriate DNS delegation until it reaches the authoritative DNS infrastructure responsible for the requested hostname.

---

### 3. The authoritative DNS server provides the DNS record

The authoritative DNS server contains the DNS records for the domain or hostname.

Depending on the hostname and configuration, DNS can contain records such as:

* **A record:** Maps a hostname to an IPv4 address.
* **AAAA record:** Maps a hostname to an IPv6 address.
* **CNAME record:** Makes one hostname an alias of another hostname.
* **TXT record:** Stores text information used for purposes such as verification.

The DNS resolver receives the appropriate response and can temporarily store it according to its **TTL (Time to Live)**.

---

## What is a CNAME record?

A **CNAME**, or Canonical Name record, creates an alias from one hostname to another hostname.

For example:

`www.example.com → example.netlify.app`

The first hostname is an alias for the second hostname.

The important point is that a CNAME points to **another hostname**, rather than directly storing an IP address.

This is useful because the target hostname can be managed by the hosting provider. If the underlying infrastructure changes, the provider can update its DNS configuration without requiring every user-facing hostname to be changed manually.

For a future custom domain, a CNAME could therefore be used to connect a hostname such as `www.example.com` to a hosting provider's hostname.

---

## 4. The browser connects to the hosting infrastructure

After DNS resolution provides the information required to reach the website, the browser connects to the appropriate hosting infrastructure.

Because the portfolio uses HTTPS, the browser establishes a secure connection using **TLS (Transport Layer Security)**.

The browser verifies the website's TLS certificate and then communicates securely with the server.

---

## 5. Netlify serves the website

Netlify receives the request and serves the deployed website files through its hosting and delivery infrastructure.

The browser then downloads the required HTML, CSS, JavaScript, images, fonts, and other assets.

The browser processes these files and renders the portfolio page on the user's device.

The complete process normally happens very quickly and is largely invisible to the user.

---

# Understanding the Deployed Project Files

I built and deployed the website using a modern frontend structure. The important project files have specific responsibilities.

### `package.json`

Defines the project's dependencies, scripts, and basic project configuration.

It allows the project to install its required packages and provides commands for development and production builds.

### `src/`

Contains the main source code for the application.

This is where the React components, application logic, styling, and other frontend source files are organized.

### React / JSX Components

The React components are responsible for individual sections and interactive parts of the portfolio.

They allow the website to be divided into reusable pieces instead of putting the entire interface into one large file.

### CSS Files

The CSS files control the visual appearance of the website, including:

* Layout
* Typography
* Spacing
* Responsive behavior
* Animations
* Component styling

### `public/`

Contains static assets that need to be served directly, such as images, icons, or other public resources.

### Entry Point

The application's entry file initializes the React application and connects the root React component to the HTML page.

### Build Configuration

The project's build configuration controls how the source code is transformed into the production assets that are deployed to Netlify.

The production build contains the files required by the browser to run the portfolio.

---

# HTTPS and Security

The live portfolio is available through HTTPS:

**https://artiwary.netlify.app/**

HTTPS protects communication between the user's browser and the website by using TLS encryption.

Netlify provides SSL/TLS certificate management for the hosted site, so the website can be accessed securely without manually purchasing and installing a certificate.

---

# Deployment

The website is deployed on Netlify and is publicly accessible without requiring visitors to log in.

The final deployment URL is:

**https://artiwary.netlify.app/**

The site can therefore be shared directly through professional platforms such as LinkedIn and included in my CV.

---

# Assignment Completion

This project fulfills the main requirements of PF-04:

* [x] Personal website created
* [x] Website publicly deployed
* [x] Website available over HTTPS
* [x] Professional positioning included
* [x] Portfolio/projects included
* [x] LinkedIn profile link included
* [x] GitHub profile link included
* [x] CV/resume access included
* [x] Contact/booking functionality included where applicable
* [x] DNS walkthrough written in my own words
* [x] DNS resolver and nameserver process explained
* [x] CNAME record explained
* [x] HTTPS/TLS process explained
* [x] Hosting and deployment process documented
* [x] Important project files and their purpose documented
* [x] Live public URL provided

## Live Deliverable

**Portfolio URL:** https://artiwary.netlify.app/

The website is publicly accessible and serves as my personal professional portfolio.

The official FlyRank completion badge will be added to the website later when the capstone is approved and the badge asset/instructions are provided.
