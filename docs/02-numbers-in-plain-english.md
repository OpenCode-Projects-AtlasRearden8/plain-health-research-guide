# Numbers in Plain English

*Odds ratios, p-values, and "3x your risk" — what those phrases actually hint, without any math degree required.*

## Start here: absolute vs. relative risk

This single concept does more heavy lifting than any other in health reporting. Get it, and half of misleading headlines wilt on the spot.

- **Absolute risk** — your actual chance of something, stated plainly. "3 in 1,000 people will experience X."
- **Relative risk** — a *ratio* comparing two groups. "Risk went up by 50%."

**Why it matters:** relative risk sounds enormous precisely because the baseline is hidden. Try these two framings of the same study:

- "New drug doubles your risk of side effect Y!" (relative)
- "Side effect Y rose from 1 in 10,000 to 2 in 10,000." (absolute)

Same data. One is a scream; the other is a shrug you can chew on. Whenever you see a percent-style claim, quietly ask: **out of how many?** If no denominator appears anywhere, the story is doing relative-risk theater.

And a gentle honesty check in the other direction: a treatment that lowers a 2-in-1,000 risk to 1-in-1,000 belongs on your radar, but "risk cut in half!" headlines rarely mention that the absolute numbers are small. Relative language shrinks and stretches the same story; absolute language tells you what you actually need.

## Odds ratios, in plain words

The **odds ratio** (OR) compares the *odds* of an outcome between two groups. It's what observational studies usually report, which is why you see it everywhere.

Plain-English decoder for an OR about an outcome (say, a disease):

| OR | What it hints |
|---|---|
| 1.0 | No difference between the groups |
| 0.5 or 2.0 | Groups differ — worth attention |
| 0.90–1.10 | About nothing, even if statistics call it "significant" |
| 3.0+ (or 0.33 and below) | Strong difference — but *still* not automatically causation |

Three honest cautions:

1. **OR ≠ risk.** Odds and probabilities are different things. When an outcome is common, an "odds ratio of 3" is *not* "3x your risk" — the real risk multiple is smaller. Headlines routinely commit this error.
2. **An OR comes from the study it comes from.** A strong OR in a small, sloppy, heavily-confounded study still belongs to a small, sloppy, heavily-confounded study.
3. **Direction matters for what it measures.** ORs below 1 mean *lower* odds — some headlines reverse this when summarizing.

## Relative risks (RR) and hazard ratios (HR)

Close cousins of the OR. Same decoder applies: ≈1 means nothing; small deviations from 1 get hyped; big deviations deserve attention **and** a look at the baseline rates (absolute risk). Hazard ratios from long-term follow-up studies compare rates over time — roughly, "at any moment during the study, group A reached the outcome at 1.2 times group B's rate."

## p-values — what people *think* they mean

A **p-value** answers one narrow question: *if there were truly no effect here, how surprising would data at least this extreme be?*

What it does **not** mean:

- ❌ "There is a 3% chance this result is wrong."
- ❌ "This proves the treatment works."
- ❌ "This means the effect is large."

What it roughly does mean:

- p < 0.05 → the result would be fairly surprising if nothing were going on (this is the conventional passing grade in most fields)
- p ≥ 0.05 → "we couldn't distinguish this from chance" — **not** the same as "proven absent"

For a friendly tour of how even scientists misread this number, Regina Nuzzo's widely shared *Nature* essay on statistical error (2014) is a good start — but the decoder above is the working version for daily life.

## Confidence intervals (CI): the wiggle room

Results often appear as: **OR 0.67 (95% CI 0.50–0.83)**.

Plain English: *"Our best estimate is 0.67, and our data is consistent with the range 0.50 to 0.83."* The wider the interval, the less certain the point estimate.

Reading rules in one line each:

- **If the CI for an OR/RR crosses 1.0** (say, 0.90–1.15), the result can't rule out "no effect." Treat it as a shrug.
- **A long skinny CI from a huge study** that barely misses 1.0 says "we're really sure about a really small difference."
- **A tight CI** is a sign of a large, precise study — respect it more.

## Sample size: how big is "big enough"?

No magic number, but some honest patterns:

| Sample size | What it can hint |
|---|---|
| Under ~30 people | Near-anecdote. Useful for "it exists," useless for "it works for you." |
| ~30–300 | Enough for early signals, especially in specialized groups. |
| ~300–3,000 | Where most "solid RCT" findings live, depending on how big the effect is. |
| Population-scale cohorts | Good for rare, long-term outcomes — but observational. |

Two honest traps:

1. **Small study + weird result ≠ breakthrough.** Small samples produce extreme readings, and early dramatic effects often shrink (or vanish) once more data comes in. Wait for the follow-up.
2. **Large study + tiny effect ≠ important for you.** A dataset of 500,000 can make a 1% relative difference "highly significant." Statistically strong; practically negligible.

Truthful guideline: significance and importance are two different dials. Headlines treat them as one.

## "Significant" — the word that causes most of the trouble

In daily English, *significant* means *important*. In statistics, *statistically significant* means *probably not a fluke at the study's chosen threshold* (often p < 0.05) — and there's a nastier implication on the other side of it: a "non-significant" result does **not** mean "no effect exists." It may mean the study was too small to reliably detect one.

A "statistically significant" result can be trivially small; an important result can be not-yet-significant because the study was small. When you see "significant" in a headline, translate it to: **"they found *some* difference."** Then go find the effect size to learn whether it's *any* difference worth caring about.

## The plain-language translator card

| When a story says… | It might mean… | Your follow-up question |
|---|---|---|
| "3x the risk" | Relative risk; baseline may be tiny | "Out of how many?" |
| "As much as an X% lower risk" | Possibly cherry-picked absolute or relative | "Starting from what baseline?" |
| "Scientists say it works" | It worked *in* this study *for these people* | "Who was studied, and how long?" |
| "No cure apart from chance" | Possibly p = 0.06 — faint signal, not zero | "What was the confidence interval?" |
| "Linked to" | Correlation, not causation | "What could confound this?" |

Keep [the full checklist](08-red-flag-checklist.html) nearby — numbers are where fishy stories most often give themselves away.

---

*One more friendly nudge: none of this is a license to dismiss all studies, and none of it is medical advice. It's a toolkit for asking better questions — including, importantly, of your own doctor.* → [Spotting Misleading Health Claims](03-spotting-misleading-claims.html)
