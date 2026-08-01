# FL-02: Prompt Iteration Log

**Intern:** Ayush Raj Tiwary | **Task selected from FL-01 audit:** Python Code Debugging (Collaborate with AI)

## The bug under test

This is a real class of bug from an ML pipeline: a moving-average helper used to smooth
sensor/data batches before feeding a model.

```python
def moving_average(data, window=3, results=[]):
    """Compute a simple moving average over `data`."""
    for i in range(len(data)):
        if i < window:
            results.append(None)
        else:
            results.append(sum(data[i-window:i]) / window)
    return results
```

**Reported symptom (used from v2 onward):** "I call `moving_average(batch)` once per
incoming data batch in a loop. Each new batch's output list is longer than it should be,
and values from old batches seem to leak into new ones."

The real bug: `results=[]` is a **mutable default argument** — Python evaluates it once at
function definition time, so every call without an explicit `results=` shares and appends
to the *same* list object. It's a classic, well-documented gotcha, which makes it a good
test case: it's *catchable* in principle, so the question is how much prompt engineering
changes the speed, precision, and reliability of catching it and proving the fix.

---

## v0 — Naive prompt (what I'd have written before this track)

**Prompt:**
> Fix this python code:
> ```
> [code above]
> ```

**Output (Claude):**
> This function has a common Python issue — using a mutable default argument
> (`results=[]`). Mutable defaults are evaluated once at function definition time, so
> they persist across calls, which can cause unexpected accumulation. Here's a cleaner
> version:
> ```python
> def moving_average(data, window=3, results=None):
>     if results is None:
>         results = []
>     for i in range(len(data)):
>         if i < window:
>             results.append(None)
>         else:
>             results.append(sum(data[i-window:i]) / window)
>     return results
> ```
> I'd also suggest adding type hints and a guard for `window <= 0`.

**Note on what happened:** It *did* catch the bug — it's famous enough that a naive prompt
still surfaces it. But the output stops there: no confirmation this is *the* bug causing
the reported symptom (there was no reported symptom to tie it to), no test proving the fix
works, no discussion of remaining edge cases (empty `data`, `window > len(data)`), and the
"also suggest" additions are generic boilerplate advice rather than targeted fixes. This is
the ceiling of what a lazy prompt gets you: a correct guess with no verification.

---

## v1 — + Role assignment

**Technique:** Give the model a specific professional identity and standard to hold itself to.

**Prompt:**
> You are a senior Python engineer doing a code review before this function ships to
> production. Review and fix this code:
> ```
> [code]
> ```

**Output (Claude):**
> Reviewing this as a production candidate, I'd block this PR. Primary issue: mutable
> default argument (`results=[]`) — this is a correctness bug, not just style, because it
> means the function's behavior depends on call history, which will cause silent data
> corruption in any long-running process. Secondary: no validation on `window` (zero or
> negative values would either loop forever in intent or silently produce wrong output);
> no handling for `len(data) < window`.
> ```python
> def moving_average(data, window=3, results=None):
>     if window <= 0:
>         raise ValueError("window must be a positive integer")
>     results = [] if results is None else results
>     for i in range(len(data)):
>         if i < window:
>             results.append(None)
>         else:
>             results.append(sum(data[i-window:i]) / window)
>     return results
> ```
> Would not approve without a unit test covering the multi-call case.

**What changed and why:** Same core fix, but the *framing* changed the standard applied.
"Production review" language pulled in validation (`window <= 0`) and explicitly named
*why* the mutable default is a correctness bug rather than a style nit, and it proactively
flagged the need for a test — none of which the naive prompt volunteered. The role didn't
change technical accuracy (it found the same bug either way); it changed thoroughness and
the severity framing.

---

## v2 — + Context and motivation

**Technique:** Explain *why* this matters and give the real symptom, not just the code.

**Prompt:**
> I have this function in a data pipeline that runs `moving_average(batch)` once per
> incoming batch, in a loop, over the course of a day. I'm seeing each batch's output
> list get longer than it should, and I suspect values from earlier batches are leaking
> into later ones. This is feeding a model that gets retrained nightly, so a silent bug
> here would corrupt training data without throwing an error. Here's the function —
> find the root cause:
> ```
> [code]
> ```

**Output (Claude):**
> That symptom is the signature of a mutable default argument. Walking through it: on
> your first call, `results` (never passed explicitly) is bound to the *same list object*
> that lives in the function's `__defaults__` — created once when the module was loaded,
> not once per call. Every subsequent call appends to that same list instead of starting
> fresh, so batch 2's output contains batch 1's values plus its own, batch 3 contains 1+2+3,
> etc. That matches "output list keeps getting longer" exactly.
>
> Fix:
> ```python
> def moving_average(data, window=3, results=None):
>     if results is None:
>         results = []
>     for i in range(len(data)):
>         if i < window:
>             results.append(None)
>         else:
>             results.append(sum(data[i-window:i]) / window)
>     return results
> ```
> Given this feeds a nightly retrain silently, I'd also add an assertion at the call site
> (`assert len(out) == len(batch)`) as a cheap tripwire so this class of bug fails loudly
> next time instead of corrupting data quietly.

**What changed and why:** This is the first version where the diagnosis is *tied to the
reported symptom* instead of a generic "this is bad practice" note — it explicitly
explains the mechanism that produces "list keeps getting longer," which the earlier
versions never connected to an observed behavior because none was given. The "silent
corruption" motivation also pulled in a defensive suggestion (the tripwire assert) that
wasn't in v0 or v1 — the model responded to *stakes*, not just correctness.

---

## v3 — + Few-shot examples

**Technique:** Show 1–2 worked examples of the input/output style you want, then apply to the real case.

**Prompt:**
> Fix bugs following this format:
>
> **Example 1**
> Bad: `def add_item(item, items=[]): items.append(item); return items`
> Bug: mutable default argument — list persists across calls.
> Fixed: `def add_item(item, items=None): items = items or []; items.append(item); return items`
>
> **Example 2**
> Bad: `def get(d, key): return d[key]`
> Bug: KeyError on missing key, no default.
> Fixed: `def get(d, key, default=None): return d.get(key, default)`
>
> Now fix this one in the same format:
> ```
> [moving_average code]
> ```

**Output (Claude):**
> Bad: `def moving_average(data, window=3, results=[]): ...`
> Bug: mutable default argument — `results` persists and accumulates across calls instead
> of starting empty each time.
> Fixed:
> ```python
> def moving_average(data, window=3, results=None):
>     results = results or []
>     for i in range(len(data)):
>         if i < window:
>             results.append(None)
>         else:
>             results.append(sum(data[i-window:i]) / window)
>     return results
> ```

**What changed and why:** The output shrank and tightened to match the exact three-line
"Bad / Bug / Fixed" shape from the examples — no production-review commentary, no
extended walkthrough, none of the extra defensive suggestions from v1/v2. It also copied a
stylistic detail from the examples verbatim: `results = results or []` instead of the
`if results is None: results = []` form used earlier (a subtle regression — `or []` would
also replace a legitimately empty-but-intentional list, whereas `is None` wouldn't). This
is the clearest evidence in the whole log that few-shot examples control *form* more
strongly than they control *content*: the model matched style so closely it imported a
mild bug ambiguity along with it.

---

## v4 — + Output structure

**Technique:** Specify the exact sections/format you want the answer broken into.

**Prompt:**
> Fix this code. Respond in exactly this structure:
> 1. **Root cause** (1–2 sentences)
> 2. **Fixed code**
> 3. **Test case** proving the bug is gone (runnable Python, using `assert`)
> 4. **Edge cases considered**
>
> ```
> [code]
> ```

**Output (Claude):**
> **1. Root cause**
> `results=[]` is a mutable default argument, evaluated once at function definition, so it
> is shared and accumulates across every call that doesn't pass `results` explicitly.
>
> **2. Fixed code**
> ```python
> def moving_average(data, window=3, results=None):
>     if results is None:
>         results = []
>     for i in range(len(data)):
>         if i < window:
>             results.append(None)
>         else:
>             results.append(sum(data[i-window:i]) / window)
>     return results
> ```
>
> **3. Test case**
> ```python
> out1 = moving_average([1, 2, 3, 4, 5])
> out2 = moving_average([10, 20, 30, 40, 50])
> assert len(out1) == 5, "first call length wrong"
> assert len(out2) == 5, "second call leaked state from first call"
> assert out2[-1] == 30.0, "second call polluted by first call's values"
> ```
>
> **4. Edge cases considered**
> - `data` shorter than `window` → every entry is `None`, no crash.
> - `window <= 0` → not currently validated; would cause `sum(data[i-0:i])` to always be
>   an empty-slice sum (0), silently wrong rather than erroring. Worth a guard if this
>   input is untrusted.
> - Empty `data` → loop doesn't execute, returns `[]` safely.

**What changed and why:** This is the first version to produce something *executable and
checkable* — a real test that specifically asserts against the mutable-default failure
mode (`out2` not being polluted by `out1`), not just "here's a fix, trust me." Forcing
"edge cases" as a mandatory section also surfaced the `window <= 0` silent-wrong-answer
case with more precision than v1's passing mention — it's now explained mechanically
(empty slice sums to 0) rather than just flagged.

---

## v5 — + Step decomposition (final combined prompt)

**Technique:** Force explicit reasoning steps before the answer, so the model diagnoses
before it prescribes.

**Prompt:**
> You are a senior Python engineer reviewing a bug report before it ships to production.
> Context: `moving_average(batch)` is called once per batch in a loop across a day; each
> batch's output list is longer than expected and seems to contain older batches' values.
> This feeds a nightly retraining job, so a silent bug corrupts training data undetected.
>
> Do this in order:
> 1. Trace through the code manually for two sequential calls — `moving_average([1,2,3,4,5])`
>    then `moving_average([10,20,30])` — and show the internal state of `results` after each call.
> 2. Based on that trace, state the root cause in one sentence.
> 3. Give the fixed code.
> 4. Give one `assert`-based test that would have caught this bug.
> 5. List any remaining edge cases not yet handled.
>
> ```
> [code]
> ```

**Output (Claude):**
> **1. Trace**
> Call 1 — `moving_average([1,2,3,4,5])`: `results` starts as the *default* list object
> (call it `L`, id constant across calls). After the loop: `L = [None, None, None, 2.0, 3.0]`.
> Returned value is `L`.
> Call 2 — `moving_average([10,20,30])`: because `results` wasn't passed, Python reuses the
> *same* `L` from before — it does **not** reset to `[]`. The loop appends three more
> entries onto the existing five, giving `L = [None, None, None, 2.0, 3.0, None, None, None]`
> (window=3 means the first two indices are `None`, and index 2 with `data[2-3:2]` on
> `[10,20,30]` is `data[-1:2]` — an empty-to-degenerate slice — so a closer trace shows this
> also produces a wrong average, not just a `None`, once mixed with prior list length; the
> important, unambiguous fact is `len(L)` is 8, not 3).
>
> **2. Root cause**
> `results=[]` is a mutable default argument; it's created once at function definition and
> reused (not reset) on every call that omits `results`, so state leaks across calls.
>
> **3. Fixed code**
> ```python
> def moving_average(data, window=3, results=None):
>     if results is None:
>         results = []
>     for i in range(len(data)):
>         if i < window:
>             results.append(None)
>         else:
>             results.append(sum(data[i-window:i]) / window)
>     return results
> ```
>
> **4. Test**
> ```python
> assert len(moving_average([10, 20, 30])) == 3, \
>     "length should reset per call, not accumulate across calls"
> ```
>
> **5. Remaining edge cases**
> - `window <= 0` is unvalidated and fails silently (empty-slice sum = 0) rather than erroring.
> - No type/length validation on `data`; a generator instead of a list would break `len(data)`.

**What changed and why:** Forcing a manual trace *before* the diagnosis caught something
the previous five versions all missed or glossed over: the interaction between the
`window` calculation and the *index math itself* once state leaks in — the trace exposed
that the leaked-state bug doesn't just make the list "longer," it changes which slices get
averaged where, which is a subtler and more accurate description of the corruption than
"values leak in" from v2. Step decomposition didn't just re-find the known bug faster; it
produced a more mechanically precise account of *how* the corruption propagates, because
the model had to commit to concrete intermediate state before writing the conclusion.

---

## Cross-model comparison (final combined prompt from v5)

**Claude's output:** see v5 above — genuinely run.

**ChatGPT's output (same v5 prompt, verbatim):**

> 1. Trace — Call 1 on `[1,2,3,4,5]`: "a new empty list is created," ends as
> `[None,None,None,2.0,3.0]`. Call 2 on `[10,20,30]`: "again, `results` is omitted, so a
> new empty list is created... the previous output is not reused, so no values leak from
> the first call," ends as `[None,None,None]`.
> 2. Root cause — mutable default argument; "every call that omits `results` shares the
> same list object... outputs accumulate across calls."
> 3. Fixed code — same fix as Claude's, plus a `window <= 0` guard baked in directly
>    (Claude only listed that as a *remaining* edge case, not a fix).
> 4. Test — `assert len(out2) == 3` and `assert out2 == [None, None, None]`.
> 5. Edge cases — window validation, empty input, window > len(data), non-`len()`-able
>    input, and a note about whether the window should include the current element.

### The specific comparison

**ChatGPT's trace directly contradicts its own root-cause explanation, and I verified this
by actually running the buggy code.** Step 1 narrates the second call as if `results`
starts fresh and empty ("no values leak from the first call") — that is a description of
the code's *behavior after the fix*, not the buggy code it was given. Step 2, one
paragraph later, correctly states the textbook mutable-default mechanism ("shares the same
list object... accumulate across calls") — which flatly contradicts what step 1 just
traced. It never reconciled the two.

This isn't cosmetic. I ran the actual unmodified buggy function:
```
call1: [None, None, None, 2.0, 3.0]
call2: [None, None, None, 2.0, 3.0, None, None, None]   # len = 8
```
ChatGPT's own assert-based test — `assert len(out2) == 3` — would **fail** against the
real buggy code it was diagnosing, because the true second-call output has length 8, not
3. It wrote a test for a version of the bug that doesn't exist.

Claude's v5 trace, while more verbose and clunkier in its prose (it hedges mid-sentence
while working out the index math), lands on the correct mechanical claim: the *same*
object persists and the second call appends onto leftover state, explicitly stating
"`len(L)` is 8, not 3" — a number I've now confirmed is exactly right.

**Other differences:**
- *Root cause quality:* both name mutable defaults correctly in isolation, but only
  Claude's is load-bearing for the rest of its own answer. ChatGPT's is right in
  isolation and wrong in context (its own trace and test contradict it).
- *Fix:* ChatGPT folded `window <= 0` validation directly into the "fixed code," where
  Claude kept the core fix minimal and listed validation separately under edge cases.
  ChatGPT's is arguably the more shippable answer here — tighter scope creep control was
  Claude's choice, not a capability gap.
- *Tone:* ChatGPT is more clipped and enumerated throughout, with less narrated reasoning
  between steps; Claude shows more of its intermediate work, which in this case is what
  caught the discrepancy — the trace was "shown," not just asserted.
- *Failure mode:* this is the real finding. ChatGPT's failure wasn't a knowledge gap (it
  knows what mutable defaults do) — it was a **verification gap**: it produced a fluent,
  confident, wrong trace and a test that would fail if actually run, and had no step that
  checked the trace against the code before writing the answer. Step decomposition only
  helps if the model actually uses the trace to constrain the final answer, rather than
  writing both independently and never cross-checking them.

---

## Final reusable template

This is the version distilled to be usable by a stranger on *any* bug, not just this one —
no personal context required, just fill the three brackets.

```
You are a senior software engineer conducting a code review before this ships to production.

Context: [describe the observed symptom or failure — what's wrong, what you expected instead,
and what's at stake if it ships broken].

Do the following in order:
1. Trace through the code manually with 2 concrete inputs that would reveal the bug. Show the
   relevant internal state after each step.
2. State the root cause in one sentence, based on the trace — not a guess before it.
3. Give the fixed code.
4. Give one assert-based test that would have caught this specific bug.
5. List any remaining edge cases the fix doesn't yet handle.

Code:
[paste code here]
```

**Why each part earns its place (traceable to the iterations above):**
- Role → raises the bar from "does it look okay" to "would this pass review," and pulls in
  validation/severity framing a neutral prompt skips (see v1).
- Context/symptom → ties the diagnosis to the actual observed failure instead of a generic
  best-practices scan (see v2).
- Step decomposition → forces a trace before a conclusion, which surfaced the most
  mechanically accurate root cause of any version (see v5).
- Structured output (test + edge cases as mandatory sections) → converts "trust me, fixed"
  into something verifiable and forces edge-case coverage rather than an afterthought
  (see v4).
- Few-shot examples were deliberately **left out** of the final template: v3 showed they
  compress output toward the example's *style* even at the cost of content precision (the
  `or []` regression) — useful when you need a consistent format across many bugs reviewed
  by different people, but not worth the risk for a one-off template meant to maximize
  correctness.