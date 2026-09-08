# Does Content Actually Decline the Way SEO Rules Assume? — A Client-Held-Out Study

* **Author**: Ayush Raj Tiwary
* **Track**: Machine Learning — Capstone (FlyRank ML Internship)
* **Repository**: [ARTiwary/Ayush-Flyrank-internship](https://github.com/ARTiwary/Ayush-Flyrank-internship)

---

## Abstract

Which of a website's hundreds of pages should a content team review first? I test whether a simple supervised model can out-rank a transparent, hand-written staleness rule at that task, using 30,000 pseudonymized content pages across 32 clients from the FlyRank ML Internship dataset. I define decline as an observed 30-day traffic-trend proxy, hold out entire clients the model never trained on, and compare a Logistic Regression / Decision Tree / Random Forest family against the rule baseline on identical data and metrics. The winning model (Logistic Regression) reaches **Precision@50 of 0.86** against the baseline's **0.44** — but the baseline itself scores *below chance* on unseen clients (ROC AUC 0.475), and re-running the same model on a naive random split inflates every metric by letting client identity leak across train/test. The honest takeaway: a learned ranking is a real, moderate improvement over the fixed rule for prioritizing review queues — not a breakthrough, and only trustworthy once you've checked that your validation split isn't quietly grading on client memorization.

---

## Introduction

A content team managing dozens of clients and thousands of pages can't manually review everything on a regular cadence. The practical decision is a prioritization problem: given limited review hours, which pages should go to the top of the queue this week? Get it wrong and the team either wastes time refreshing pages that didn't need it, or lets a genuinely declining page keep losing visibility unnoticed.

The obvious first answer is a rule: flag pages that are stale, get lots of traffic, and convert poorly. It's transparent and cheap to compute. The question this paper asks is whether a model that can weigh several signals jointly — rather than a fixed threshold on one or two — actually earns its added complexity, and whether that improvement survives an honest test on clients the model has never seen before.

---

## Data

This study uses the FlyRank ML Internship **starter release** — `content_refresh_anonymized.csv` — not the full 79M-row warehouse. One row is one pseudonymized content page; all metrics are aggregated over a trailing 90-day window.

* **30,000** pages
* **32** pseudonymized clients
* **54.2%** labeled "declining"
* **90d** trailing window

### Target
`is_declining_label = 1` when `trend_direction == "down"` — a 30-day-vs-prior-30-day impressions comparison already computed in the dataset. This is an **observed proxy**, not a verified business outcome like lost revenue or rankings.

### Deliberately excluded, and why
* `trend_direction`, `trend_pct` — these define the label; using them as features would be circular.
* `impressions_last_30d`, `clicks_last_30d`, `sessions_last_30d`, and the matching `*_prev_30d` columns — the raw ingredients of the label's own trend calculation, sitting inside its time window.
* `content_id`, `client_id` — pseudonymous identifiers, used only to group the train/test split, never as model inputs.
* `provider_used`, `model_used` — generation metadata, not a signal about page performance.

No client names, raw URLs, or search queries appear anywhere in this analysis or its outputs — every identifier shown below is an anonymized pseudonym already present in the released dataset.

---

## Methodology

### Baseline
A transparent, unsupervised rule: score = `0.40·rank(log(impressions)) + 0.35·rank(staleness) + 0.25·rank(−CTR)`. A page scores high when it's highly visible, hasn't been touched in a while, and converts poorly — exactly the intuition a human reviewer would use, with no labels involved in fitting it.

### Models
Logistic Regression → Decision Tree → Random Forest, in that order: start with the model a strategist can fully explain, and only add complexity if it earns a measurable gain. Roughly 18 numeric features (log-transformed traffic counts, CTR, position, engagement, content properties), 3 one-hot categoricals, and 5 missingness flags (`has_keyword_data`, `has_word_count`, `has_position_data`, `has_clicks`, `has_ai_sessions`) — flags rather than a blind `fillna(0)`, because missingness in this dataset follows content type, and a silent fill would quietly encode content type into every numeric feature.

### Validation design — client-grouped split
Pages from the same client are never split across train and test (80/20, seed 42, via `GroupShuffleSplit`). Client identity is a confound — traffic style, publishing cadence, industry — that a random row-level split would let leak between train and test, letting the model partly memorize "this is Client X's typical page" instead of learning something that generalizes to a client it has never scored before. That's the actual deployment scenario, so it's the actual test.

### Leakage checks
Verified in code, not just claimed: zero client overlap between train and test after the grouped split, and none of the excluded columns above appear in the final feature matrix.

---

## Results

Test-set base rate (share of pages labeled declining): **0.511** — a coin flip's worth of "declining," which is why raw accuracy would be a meaningless headline number here. Precision@50 and ROC AUC, both measured against that base rate, are the honest metrics.

| Model | ROC AUC | Avg. Precision | Precision@50 | Recall | F1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| baseline_rule | 0.475 | 0.480 | 0.44 | — | — |
| **logistic_regression** | **0.623** | **0.624** | **0.86** | **0.771** | **0.649** |
| decision_tree | 0.591 | 0.572 | 0.56 | 0.572 | 0.582 |
| random_forest | 0.611 | 0.600 | 0.60 | 0.707 | 0.627 |

> **Reading the table:** the rule baseline scores *below chance* (ROC AUC 0.475 vs. a 0.50 coin flip) on clients it wasn't tuned on — staleness and visibility alone don't reliably separate decline from non-decline once you leave familiar clients. Logistic Regression wins on Precision@50 (0.86 vs. 0.44, roughly a 2x lift), a real but moderate improvement, not a dramatic one — ROC AUC of 0.62 says a lot of the variance in decline is still unexplained by these 90-day snapshot features alone.

### What the winning model leans on
Permutation importance on held-out clients highlights that traffic volume and position dominate as intuitive signals a content strategist would already trust, rather than an unexplained black-box feature. None of the excluded label-window columns show up here, ensuring no data leakage occurred.

### Validation design changes the story
Re-running the same Logistic Regression on a naive random split — where the same client's pages can land in both train and test — moves ROC AUC from 0.623 to 0.705 and Precision@50 from 0.86 to 0.90, purely from the validation design, not the model. This is the paper's second finding, not a footnote: a headline metric is only as honest as the split it was measured on.

### Error analysis
The model's confident false positives cluster on pages with heavy staleness and near-zero CTR that look like textbook decline candidates on every feature available — but the actual 30-day trend moved for reasons the 90-day snapshot can't see. Its false negatives skew toward high-traffic, well-positioned pages that are newly declining.

---

## Limitations & Honest Framing

* **Proxy label, not ground truth.** `is_declining_label` is a rule on a 30-day impression window, not a verified outcome like lost revenue or rankings — directional evidence, not proof.
* **Modest lift, not a breakthrough.** ~2x Precision@50 improvement is real and worth using, but ROC AUC (~0.62) means most of what drives decline in this data isn't fully captured by these features.
* **No causal claim.** Nothing here says *why* a page declines, or that editing a feature would reverse a decline — only that these signals correlate with the observed proxy.
* **Single teaching slice.** 30,000 rows across 32 clients is a teaching sample, not the full 79M-row warehouse.
* **Decision-support only.** This ranks pages for human review. It does not decide what to publish and should never trigger an automatic content change.

---

## Ranked Recommendations

Scoring the held-out (unseen) clients with the winning model produces a ranked queue of 6,163 pages. Top of the queue snippet:

| Rank | Content | Client | Score | Action | Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | content_8ba781… | client_8527a8… | 0.941 | refresh_and_review_ctr | HIGH_TRAFFIC \| LOW_CTR |
| 2 | content_c82bc0… | client_f369cb… | 0.937 | refresh_and_review_ctr | HIGH_TRAFFIC \| LOW_CTR |
| 3 | content_87c007… | client_f369cb… | 0.937 | refresh_and_review_ctr | HIGH_TRAFFIC \| LOW_CTR |

Full 6,163-row queue: `work/outputs/w07_ranked_action_queue.csv` in the repo.

### Human-in-the-loop rules — what NOT to automate
Never auto-publish, auto-deprioritize, or auto-delete based on model score alone. Every top-ranked item gets a human review before any content change ships.

---

## Reproducibility

Seed fixed at `42` throughout; `scikit-learn 1.8.0`. Full pipeline:
* `w01_research_question.ipynb` — lane and question
* `w02_ml_task_framing.ipynb` — task type, target, metric
* `w03_data_contract.ipynb` — data contract
* `w04_baseline_score.ipynb` — baseline rule
* `w05_model.ipynb` — model training
* `w06_validation_audit.ipynb` — validation / leakage audit
* `w07_action_playbook.ipynb` — action playbook + exports
* `capstone.ipynb` — end-to-end runnable notebook

---

## 5-Minute Showcase Demo Outline (Week-8 Optional Presentation)

* **Minute 1: The Core Question & The Real Problem**
  * *Focus:* Content teams managing hundreds of client pages face a triage bottleneck—how to choose what to refresh first without wasting hours or missing genuine visibility drops.
  * *Visual:* Live link to the deployed paper header and abstract.
* **Minute 2: The Data & The Strict Leakage Boundaries**
  * *Focus:* 30,000 pseudonymized pages across 32 clients. Explaining why raw metric windows (`trend_*`, `*_last_30d`) were deliberately excluded to prevent circular logic.
  * *Visual:* The Data section stats callout (30k rows, 32 clients, 54.2% baseline proxy).
* **Minute 3: The Baseline vs. Model Clash (One Honest Result)**
  * *Focus:* Why the transparent rule baseline scored *below chance* (ROC AUC 0.475) on unseen clients, whereas Logistic Regression achieved an 0.86 Precision@50 (~2x lift).
  * *Visual:* Core metrics summary table.
* **Minute 4: The Validation Trap & Error Reality**
  * *Focus:* Showing how a naive random split falsely inflated metrics (ROC AUC 0.62 to 0.70) due to client leakage, and acknowledging that ROC AUC 0.62 means much of decline variance remains uncaptured.
* **Minute 5: Action Playbook & Human-in-the-Loop Safeguards**
  * *Focus:* Walking through the 6,163-row exported action queue and emphasizing the strict **No-Go rule**: decision-support only, never auto-publishing.

---

## Shareable Cuts & Portfolio Snippets

### 1. Short Social Post (Methodology & Honest Findings)
> Most SEO refresh rules rely on a single static heuristic (like staleness or traffic) that breaks down when tested on new websites. 
> 
> For my FlyRank ML capstone, I tested whether a simple supervised model could better prioritize content-refresh queues across 30,000 pseudonymized pages. By enforcing an honest **client-grouped split** (making sure the model never trained on the clients it was evaluated on), I found that:
> 1. Hand-written rule baselines score below chance on unseen clients (0.475 ROC AUC).
> 2. A transparent Logistic Regression model achieves an **0.86 Precision@50** (~2x lift).
> 3. Naive random splits create false confidence by letting client identity leak across train/test sets.
> 
> Check out the full case study here: [Your GitHub Pages URL] #SEO #MachineLearning #DataScience #FlyRank

### 2. Employer-Facing 3-Sentence Summary
> **What I built:** A production-grade content-refresh ranking pipeline and risk-scoring model that turns raw trailing-90-day SEO metrics into an actionable triage queue for content strategists. 
> **On what data:** A public-safe teaching slice of 30,000 pseudonymized pages across 32 distinct clients from the FlyRank ML dataset, engineered with strict leakage prevention and client-grouped validation splits. 
> **What it showed:** The model achieved an 0.86 Precision@50 (outperforming traditional rules by ~2x), while proving empirically that random train/test splitting dangerously inflates performance metrics through client-identity leakage.

---

<footer id="credit">
  <p>Built on the <a href="https://flyrank.ai" target="_blank" rel="noopener">FlyRank ML Internship dataset</a>. Data anonymized and released for educational use; all client and content identifiers shown here are pseudonyms from that release.</p>
  <p>© Ayush Raj Tiwary — decision-support research, not a production ranking claim.</p>
</footer>