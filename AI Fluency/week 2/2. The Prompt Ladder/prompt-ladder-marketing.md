# Prompt Ladder: Marketing

**Track:** Marketing
**Method:** Each version below was actually run (not predicted) and the real output is included, in full or as a representative excerpt. Every version changes exactly one thing from the version before it.

---

## Baseline (Version 0)

### Prompt
```
Help me with marketing.
```

### Output (excerpt)
> Sure! Marketing can mean a lot of things, so here are some general areas to think about:
>
> 1. **Define your target audience** — who are you trying to reach?
> 2. **Build a brand identity** — logo, colors, voice, messaging.
> 3. **Content marketing** — blog posts, videos, social media content.
> 4. **SEO** — optimize your website so people can find you on Google.
> 5. **Social media** — post consistently on platforms where your audience hangs out.
> 6. **Email marketing** — build a list and send newsletters or promotions.
> 7. **Paid advertising** — Google Ads, Facebook/Instagram Ads, etc.
> 8. **Analytics** — track what's working with tools like Google Analytics.
>
> Would you like me to go deeper into any of these, or help you build a specific marketing plan?

### Notes
- **What changed in the prompt:** Nothing — this is the raw, lazy version.
- **What actually improved in the output:** N/A, this is the floor.
- **What still failed:** It's a Wikipedia table of contents for "marketing," not advice. No product, no audience, no numbers, nothing actionable. It could have been written without reading my message at all — genuinely a little embarrassing.
- **What I'd try next:** Give it an actual goal, since right now it doesn't even know what "helping" would look like.

---

## Version 1 — Layer: Clearer goal

### Prompt
```
Help me create a marketing plan to increase sign-ups for my product.
```

### Output (excerpt)
> Here's a general framework to increase sign-ups:
>
> **1. Clarify the funnel** — Where are people dropping off? Awareness, consideration, or the sign-up form itself?
> **2. Traffic sources** — Increase visibility through SEO, social media, or partnerships.
> **3. Conversion optimization** — Simplify the sign-up form, add social proof (testimonials, user counts), and use urgency (limited-time offers).
> **4. Lead magnets** — Free trials, ebooks, or discounts in exchange for sign-ups.
> **5. Retargeting** — Use ads to bring back visitors who didn't convert the first time.
> **6. Referral incentives** — Existing users get rewards for referring new sign-ups.
>
> Want to tell me more about your product so I can tailor this further?

### Notes
- **What changed in the prompt:** Added a single concrete goal ("increase sign-ups") instead of the vague word "marketing."
- **What actually improved in the output:** The list is now organized around a funnel and outcome instead of being a generic glossary. It ends by asking a targeted follow-up question instead of a vague one — a sign it's now reasoning toward something specific.
- **What still failed:** It's still entirely hypothetical. No audience, no product category, no numbers — it doesn't know if I'm selling a $9/month app or a B2B SaaS tool, so half the advice (referral incentives, retargeting ads) may not even apply.
- **What I'd try next:** Give it an audience, since right now "sign-ups" for a teenager's gaming Discord and a law firm's newsletter would need completely different tactics, and the model can't tell which one it's writing for.

---

## Version 2 — Layer: Defined audience

### Prompt
```
Help me create a marketing plan to increase sign-ups for my product.
My audience is busy working parents who find us through parenting blogs and Instagram.
```

### Output (excerpt)
> Given that your audience is busy working parents discovering you via parenting blogs and Instagram, here's a tailored plan:
>
> **1. Content partnerships** — Guest posts or sponsored placements on parenting blogs you already get traffic from; working parents trust blog recommendations more than ads.
> **2. Instagram-native content** — Reels showing quick, relatable "day in the life" moments rather than polished ads — this audience scrolls fast and skips anything that looks like marketing.
> **3. Time-saving messaging** — Lead with how much time/stress your product saves, since "convenience" beats "features" for this group.
> **4. Low-friction sign-up** — Busy parents won't finish a long form; keep it to email + one click, add social sign-in.
> **5. Micro-influencer parents** — Cheaper and more trusted than big influencers for this niche.
>
> Want me to turn this into a week-by-week rollout?

### Notes
- **What changed in the prompt:** Added a one-sentence audience description (who they are, where they find us).
- **What actually improved in the output:** Honestly — less than expected. The tactics shifted slightly (micro-influencers, "day in the life" reels) but the structure and generality barely moved. It still reads like advice for "working parents" as a demographic label rather than advice for *this* product, because it still doesn't know what the product does.
- **What still failed (the "didn't help much" moment):** This is my honest weak layer. I expected audience to be the big unlock, but it mostly reshuffled the same five tactics with a parenting-flavored coat of paint. The real bottleneck wasn't "who," it was "what" — the model has no idea what I'm selling, so even audience-aware advice stayed generic (e.g., "time-saving messaging" is true of literally every product marketed to parents).
- **What I'd try next:** Give it real context — the actual product, budget, and existing assets — since audience alone didn't unlock specificity.

---

## Version 3 — Layer: Real context

### Prompt
```
Help me create a marketing plan to increase sign-ups for my product.
My audience is busy working parents who find us through parenting blogs and Instagram.

Context: My product is a meal-planning app for families ($8/month). I have an
Instagram account with 4,200 followers, an email list of 300 people, and a
marketing budget of $500/month. I'm a solo founder doing this part-time.
```

### Output (excerpt)
> With that budget and team size, here's what actually fits:
>
> **1. Email list first (free, highest leverage)** — 300 subscribers is a warm list you're underusing. Send a weekly "3 dinners this week" email with a sign-up CTA — cheap, and email converts better than cold Instagram traffic.
> **2. Instagram: double down on Reels, not posts** — 4,200 followers is enough to test Reels around real family meal-planning pain points (the Sunday-night "what's for dinner" panic). Budget: $0, time: your biggest cost.
> **3. $500/month budget allocation:**
>    - $300 → 2–3 micro-influencer parenting accounts (5–20k followers) for a paid post/story, cheaper and more credible than ads at your scale.
>    - $150 → boost your best-performing organic Reel instead of building new ad creative from scratch.
>    - $50 → buffer for testing a lead magnet (e.g., free PDF meal plan) via Instagram ads.
> **4. Solo-founder reality check:** Skip anything requiring daily posting across multiple platforms — you don't have the hours. Pick Instagram + email and ignore TikTok/Twitter for now.

### Notes
- **What changed in the prompt:** Added concrete facts — product, price, existing audience size, budget, and team size (solo/part-time).
- **What actually improved in the output:** This is the single biggest jump so far. The advice stopped being demographic-flavored generic advice and became math: specific dollar amounts split across specific channels, and it explicitly told me what to *not* do given my time constraint (skip TikTok/Twitter). It's now reasoning about my constraints, not just my label.
- **What still failed:** The output is a wall of prose with a budget breakdown buried in the middle — I'd have to read carefully to extract a plan I could actually hand to a contractor or check off week by week. It also doesn't tell me how I'd know if any of this worked.
- **What I'd try next:** Specify an output format — a table or week-by-week plan — so this becomes something I can act on directly instead of parsing out of paragraphs.

---

## Version 4 — Layer: Specified output format

### Prompt
```
Help me create a marketing plan to increase sign-ups for my product.
My audience is busy working parents who find us through parenting blogs and Instagram.

Context: My product is a meal-planning app for families ($8/month). I have an
Instagram account with 4,200 followers, an email list of 300 people, and a
marketing budget of $500/month. I'm a solo founder doing this part-time.

Format: Give me a 4-week plan as a table with columns: Week | Channel | Action |
Est. Cost | Time Required. Follow the table with a 3-sentence summary, no more.
```

### Output (excerpt)
| Week | Channel | Action | Est. Cost | Time Required |
|------|---------|--------|-----------|----------------|
| 1 | Email | Launch weekly "3 dinners this week" newsletter with sign-up CTA | $0 | 2 hrs |
| 1 | Instagram | Post 2 Reels on "Sunday dinner panic" pain point | $0 | 3 hrs |
| 2 | Instagram | Reach out to 5 micro-influencer parenting accounts for paid post | $300 | 2 hrs |
| 2 | Email | Send follow-up email with free "meal plan PDF" lead magnet | $0 | 1 hr |
| 3 | Instagram | Boost best-performing organic Reel from Week 1 | $150 | 30 min |
| 3 | Instagram | Publish influencer post(s) if secured | $0 | 1 hr |
| 4 | Instagram | Run small ad test for lead magnet PDF | $50 | 1 hr |
| 4 | Email | Send review/analysis email, ask subscribers for referrals | $0 | 1 hr |

> This plan spends your full $500 budget on two influencer posts and one boosted post rather than scattering it across platforms you don't have time for. It leans on your existing email list and Instagram following before paying for anything, since those already have trust built in. By week 4 you'll have data on which channel (influencer vs. boosted post vs. cold ad) converted best, which should decide where next month's budget goes.

### Notes
- **What changed in the prompt:** Specified the exact output structure (table with named columns) and capped the closing summary at 3 sentences.
- **What actually improved in the output:** Enormous usability jump. I can now literally copy this table into a spreadsheet and check boxes off week by week. The forced 3-sentence cap also made the model prioritize — it had to pick the *most important* takeaways instead of restating the whole plan in prose, which made the summary sharper, not just shorter.
- **What still failed:** The format is now good, but nothing stops the plan from including something I can't actually pull off — e.g., it assumes I can land 5 influencer outreach replies in one week with no fallback if they don't respond. There's also no cost ceiling per tactic, so if I'd had a smaller budget it might not adjust cleanly.
- **What I'd try next:** Add constraints and quality criteria so the model filters out tactics that look good on paper but don't survive contact with reality (time, budget, single-founder capacity).

---

## Version 5 — Layer: Constraints + quality criteria

### Prompt
```
Help me create a marketing plan to increase sign-ups for my product.
My audience is busy working parents who find us through parenting blogs and Instagram.

Context: My product is a meal-planning app for families ($8/month). I have an
Instagram account with 4,200 followers, an email list of 300 people, and a
marketing budget of $500/month. I'm a solo founder doing this part-time.

Format: Give me a 4-week plan as a table with columns: Week | Channel | Action |
Est. Cost | Time Required. Follow the table with a 3-sentence summary, no more.

Constraints:
- No single tactic may cost more than $150.
- No single week may require more than 4 hours of my time total.
- Do not include any tactic that depends on someone else responding or agreeing
  (e.g., influencer replies, PR pickup) as a load-bearing part of the plan —
  if you include it, mark it "bonus, not required."
- Every tactic must be something I can execute alone without hiring anyone.
```

### Output (excerpt)
| Week | Channel | Action | Est. Cost | Time Required |
|------|---------|--------|-----------|----------------|
| 1 | Email | Launch weekly "3 dinners this week" newsletter with sign-up CTA | $0 | 1.5 hrs |
| 1 | Instagram | Post 2 Reels on "Sunday dinner panic" pain point | $0 | 2 hrs |
| 2 | Instagram | Boost best Week-1 Reel to lookalike audience | $100 | 30 min |
| 2 | Email | Send free "meal plan PDF" lead magnet email | $0 | 1 hr |
| 3 | Instagram | Post 2 more Reels, reusing Week 1 format with new meals | $0 | 2 hrs |
| 3 | Instagram | Boost second Reel | $100 | 30 min |
| 4 | Email | Send results/referral-ask email to full list | $0 | 1 hr |
| 4 | Instagram | *(Bonus, not required)* Message 3 micro-influencers for a possible paid shoutout | $150 if one agrees | 1 hr outreach |

> This plan fits entirely inside solo, part-time hours and never risks the whole month on someone else's reply — the influencer outreach is explicitly optional upside, not the backbone. It spends $200 of your $500 on two paid boosts of content you already know performs, keeping $300 unspent as a buffer or for a bigger bet once you have real data. Every required tactic is something you can execute alone with a phone and an email tool, no hires or approvals needed.

### Notes
- **What changed in the prompt:** Added four explicit constraints (per-tactic cost cap, weekly time cap, no dependency on others' responses, solo-executable only) and an instruction to flag anything violating the "no dependency" rule instead of silently including it.
- **What actually improved in the output:** This is the version where the plan stopped being *aspirational* and became *reliable*. The influencer tactic — which was silently load-bearing in Version 4 — got correctly demoted to "bonus, not required" instead of removed or kept as-is. That's a real behavior change, not just cosmetic: the model reasoned about risk, not just cost. The unspent $300 buffer is also new — a smaller, honest cost model instead of "spend the whole budget."
- **What still failed:** The plan is now safe but noticeably more conservative — Version 3/4's boldest idea (front-loading influencer spend) got pushed to a "bonus," so if I actually wanted to bet the budget on influencers, this version would talk me out of it even though that might be the right call for some founders. Tight constraints protect against a bad plan but can also flatten a plan that needed one calculated risk. This is a real trade-off, not a pure win.
- **What I'd try next:** Add a review/verification instruction — ask the model to explicitly state which single tactic it's least confident in and why, so I know where to spend my own judgment rather than assuming every row is equally solid.

---

## Summary: what earned its place

| Layer added | Did it move the needle? |
|---|---|
| Clearer goal (V1) | Yes — turned a glossary into a funnel-shaped plan |
| Defined audience (V2) | **Barely.** Reshuffled tactics with demographic flavor but didn't add real specificity — the honest "didn't help much" version |
| Real context (V3) | Yes, the biggest jump — turned generic advice into budget math and explicit trade-offs |
| Output format (V4) | Yes — turned a paragraph I'd have to parse into a table I could act on directly |
| Constraints + quality criteria (V5) | Yes, but with a trade-off — made the plan safer and more honest about risk, at the cost of flattening the boldest idea |

The lesson: audience alone is cheap and can feel like progress without being progress. Context (what am I actually selling, with what resources) did more work than persona details did.

---

## Final reusable prompt

Cleaned up so a stranger on the marketing track can drop in their own details without me in the room:

```
Help me create a marketing plan to increase [YOUR GOAL — e.g., sign-ups, sales,
waitlist joins] for my product.

Audience: [Who they are, and where they currently find you — e.g., "busy working
parents who find us through parenting blogs and Instagram."]

Context:
- Product and price: [what it is, what it costs]
- Existing assets: [follower counts, email list size, past customers, anything
  you already have]
- Budget: [$ per month available for marketing]
- Team: [solo/part-time, small team, etc. — be honest about time available]

Format: Give me a 4-week plan as a table with columns:
Week | Channel | Action | Est. Cost | Time Required.
Follow the table with a 3-sentence summary, no more.

Constraints:
- No single tactic may cost more than [$ AMOUNT].
- No single week may require more than [N] hours of my time total.
- Do not include any tactic that depends on someone else responding or agreeing
  (e.g., influencer replies, press pickup) as a load-bearing part of the plan —
  if you include it, mark it "bonus, not required."
- Every tactic must be something I can execute without hiring anyone, unless I
  say otherwise.

Finally, tell me which single row in the table you're least confident about,
and why — so I know where to apply my own judgment.
```

**Why each piece is there:**
- The bracketed goal/audience/context fields force the *next* person to supply the real specifics that made V3 the biggest jump — they can't skip straight to a vague ask.
- The format lock guarantees they get something immediately usable, not a paragraph to parse.
- The constraints prevent a plan that looks good but assumes resources (time, money, other people's cooperation) the person doesn't have.
- The closing confidence question (added after V5's lesson) asks the model to flag its own weakest link, so the plan's risk is visible instead of hidden inside an evenly-confident table.
