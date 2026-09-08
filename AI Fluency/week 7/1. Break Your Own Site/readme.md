# General AI Fluency: Assignment Submission

**Week 7 Track:** Break Your Own Site
**Student Name:** Ayush Raj Tiwary

**Live Portfolio:** https://artiwary.netlify.app/
**GitHub Repository:** https://github.com/ARTiwary/portfolio

## 1. The “Where It Breaks” Stress-Test Log

To go beyond the happy path, I deliberately stress-tested my portfolio across edge cases, including empty form submissions, malformed input, rapid double-clicks, and unusual viewport sizes.

| **Test Vector**                        | **Action Taken**                                                        | **Observed Failure / Crack**                                                                                                 | **Triage Status**                                                                                                      |
| -------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Empty Form Submission**              | Clicked submit on the contact form with all fields blank.               | Browser-native HTML5 validation caught the empty fields, but custom state feedback messages were absent on mobile viewports. | **Fix-Now**                                                                                                            |
| **Garbage / Malformed Input**          | Entered random special characters (`$%^&*!@#`) into the email field.    | Basic string matching accepted invalid email formats without providing a client-side format warning.                         | **Fix-Now**                                                                                                            |
| **Rapid Double-Submission**            | Clicked the contact form submit button twice in rapid succession.       | Duplicate network requests could be sent before the loading spinner disabled the button state.                               | **Fix-Now**                                                                                                            |
| **Out-of-Bounds Viewport (Foldables)** | Tested on an unusually narrow foldable-style viewport at `280px` width. | Secondary subtitle text in the hero section wrapped awkwardly, causing a minor horizontal layout shift.                      | **Known Limitation** — Minor visual issue on ultra-narrow sub-300px viewports; deferred to a future maintenance patch. |

## 2. SEO, Meta Tags, and Performance Audit

### SEO & Open Graph

I added comprehensive metadata inside `index.html` to improve search visibility and ensure professional social-share previews across platforms such as LinkedIn, Twitter/X, and messaging applications.

* **Page Title:** `Ayush Raj Tiwary — AI/ML Engineer & Full-Stack Developer`
* **Meta Description:** `Portfolio of Ayush Raj Tiwary, showcasing production-grade AI/ML models, Groq-powered RAG apps, and full-stack React systems.`
* **Open Graph Tags:** Configured `og:title`, `og:description`, `og:image`, and `og:url` for rich social preview cards.

### Findability Check

Verified that searching for **“Ayush Raj Tiwary Portfolio”** correctly surfaces the live Netlify production portfolio as the primary result.

### Performance Check

Ran performance audits to evaluate initial page rendering and asset delivery. The portfolio demonstrated fast initial loading, with optimized assets served through Netlify's CDN.

## 3. Triage & Fix Implementation

Following the stress test, I updated the codebase and deployed the fixes directly to production. The three **Fix-Now** issues were addressed as follows:

### 1. Robust Email Validation

Integrated stricter regex-based email validation alongside native HTML5 validation. Malformed email entries are now identified immediately on the client side before a network request is made.

### 2. Submit Button Debouncing

Added a loading-state toggle using `isSubmitting`. The submit button is disabled immediately after the first submission attempt, preventing rapid repeated clicks from generating duplicate form requests.

### 3. Enhanced Feedback States

Added explicit inline error and success banner messages so visitors receive immediate visual feedback when interacting with the contact form. This provides clearer confirmation of whether an action succeeded or requires correction.

## 4. Final Stress-Test Outcome

The Week 7 stress test shifted the focus from simply making the portfolio work to deliberately trying to make it fail.

The main issues discovered during testing were:

* Missing custom feedback for empty form submissions.
* Insufficient client-side validation for malformed email input.
* Potential duplicate form submissions from rapid clicks.
* A minor layout quirk on extremely narrow `280px` viewports.

The three actionable failures were fixed and deployed, while the ultra-narrow viewport issue was documented as a known limitation for a future maintenance pass.

## 5. Assignment Takeaway

The exercise demonstrated that a production website should be tested against failure conditions, not only its intended “happy path.” By deliberately submitting bad data, triggering repeated actions, and testing extreme viewport dimensions, I was able to identify weaknesses that were not obvious during normal usage.

AI-assisted auditing helped structure the investigation around **what could break, why it could break, and how it should be fixed**. The resulting fixes improved the portfolio's form reliability, user feedback, validation behavior, and overall resilience.
