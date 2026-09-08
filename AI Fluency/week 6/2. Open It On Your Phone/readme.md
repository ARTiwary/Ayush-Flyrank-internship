# Open It on Your Phone — Fix Log & Assignment Documentation

**Student Name:** Ayush Raj Tiwary
**Track / Phase:** General AI Fluency • Week 6: Open It on Your Phone (Build+ Phase)

**Live Portfolio:** https://artiwary.netlify.app/
**GitHub Repository:** https://github.com/ARTiwary/portfolio

## 1. Mobile & Cross-Device Audit Summary

For this assignment, I opened my live portfolio on a real mobile device and tested responsive breakpoints to audit layout behavior, touch targets, contrast, and performance.

Using AI-assisted auditing with questions such as **“What’s broken on mobile, what’s the accessibility problem, and why is this slow?”**, I identified and resolved common mobile responsiveness issues. Images were optimized, touch-target padding was expanded for mobile ergonomics, contrast ratios were verified, and every project demo and GitHub repository link was manually clicked and confirmed active.

## 2. The Fix Log — Before / After Notes

| **Component / Area**         | **What Was Broken (Before)**                                                                                                                                            | **What I Changed (After)**                                                                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Hero & Header Layout**     | The top badge cluster and hero banner text suffered from horizontal overflow on smaller screen widths, particularly on iPhone-sized viewports, causing text truncation. | Applied responsive flex-wrap rules, adjusted padding, and reduced container padding so badges stack cleanly without spilling outside the viewport.                                               |
| **Project Card Buttons**     | Live Demo and GitHub buttons were too tightly packed and had small hit areas, leading to accidental mis-taps on mobile touchscreens.                                    | Increased button touch targets with `padding: 10px 16px`, added spacing between buttons, and ensured minimum interactive target sizes of 48×48px.                                                |
| **Image Assets & Scaling**   | Project thumbnail images loaded as full-size, uncompressed assets, contributing to layout shifts and slower initial paint on mobile data connections.                   | Compressed oversized project images and added fluid CSS rules such as `max-width: 100%; height: auto;` to prevent images from overflowing their containers.                                      |
| **Typography & Readability** | Paragraph text and project descriptions felt cramped on smaller viewports because of tight line heights, reducing legibility against the dark background.               | Adjusted base font scaling and set line-height to `1.6`, while improving contrast ratios for more comfortable reading on mobile and OLED screens.                                                |
| **Link Integrity Check**     | Outbound links needed to be verified to ensure there were no dead references.                                                                                           | Confirmed that all three featured projects—MRI Tumor Detection, Smart Dining Assistant, and Air Gesture Recognition—successfully point to their live deployments and active GitHub repositories. |

## 3. Mobile Audit Outcome

The mobile audit addressed the primary usability and responsiveness issues found during real-device testing:

* **Responsive layout:** Removed horizontal overflow and improved stacking behavior on narrow screens.
* **Touch usability:** Increased interactive button areas and spacing to reduce accidental taps.
* **Image performance:** Reduced unnecessary image weight and prevented image overflow.
* **Readability:** Improved typography, line spacing, and contrast for mobile users.
* **Link reliability:** Manually verified the live demo and repository links for all three featured projects.

These changes improved the portfolio's overall mobile experience while maintaining the existing desktop layout and visual design.

## 4. Assignment Takeaway

This audit reinforced the importance of testing a deployed website on an actual mobile device rather than relying only on a desktop browser or responsive preview. AI-assisted review helped identify potential accessibility, performance, and responsive-design issues, while real-device testing provided confirmation that the fixes worked in practice.

The final result is a portfolio that is more responsive, accessible, touch-friendly, and reliable across smaller screen sizes.
