# Use AI to Translate — Then Verify

*An AI chatbot is the world's most patient translator of jargon. It's also confidently wrong sometimes. Here's how to get the good without the bad.*

## Why this works (and where it stops working)

You already know the loop: a paper mentions "non-inferiority margin," you look it up, you hit a page written by statisticians for statisticians, you close the tab all twelve times.

An AI assistant fixes the *lookup* part. Ask it to explain a term "like a friend would" and it will — instantly, gently, as many times as you like. For learning vocabulary and getting oriented, that's substantial progress.

What an AI assistant does **not** reliably do:

- Read the actual numbers in a paper and reason about them flawlessly
- Stay up to date (its knowledge has a cutoff date)
- Resist the pull of your expectations — if you phrase a question assuming the study says something, it may agree with you
- Replace your care team (this manual is education, not medical advice; so is an AI chat session)

So the workflow is: **AI first for translation, you second for verification.** Verification is easier than it sounds, because the two steps use entirely different tools.

## Step 1 — De-jargonizing a paper

Copy the jargon-heavy paragraph — just the *technique-y* part, ideally — into an AI chat and use a prompt like:

> "Explain this paragraph in plain English, at roughly an educated-adult level. Define every technical term the first time it appears, briefly. Do not add any claims that aren't in the paragraph. If a sentence is ambiguous, say so instead of guessing. End with: 'anything here still unclear?'"

The last two instructions matter. Telling it *not to add claims* reduces overconfidence, and inviting it to admit ambiguity gets you honesty instead of fluent nonsense.

Good follow-ups, in order:

1. *"What study design is this, and what are the limits of that design?"*
2. *"Translate the odds ratio of 0.67 into an absolute-risk-style sentence for someone with no stats background."*
3. *"What question would a skeptical doctor ask about this study?"*

## Step 2 — Verifying the AI (the part most people skip)

You can verify everything from Step 1 with the toolkit you've already built:

- **The definition check.** Ask a *second* AI session (or a fresh chat) the same question with different wording. If the two explanations disagree about what "non-inferiority" means, you have a conflict to resolve — usually by checking the glossary in a textbook-level source or the [glossary in this manual](09-glossary.html).
- **The paper check.** Whatever the AI claims the paragraph says, hold the paragraph itself against it. AI summaries drift toward tidy conclusions; the abstract has the sloppier, truer wording.
- **The search check.** For any factual claim about the *state of the world* ("this was replicated in 2023"), verify against a real search or an indexed database — not the model's memory.
- **The direct-quote trick.** The single most effective prompt upgrade: ask it to quote exact lines.

> "Quote the exact sentence(s) from this abstract that support your summary. If no sentence supports it, say so."

An AI that must quote verbatim is dramatically less slippery, because you can check the quote against your own eyes.

## Step 3 — Using AI on the *headline*, not just the paper

A fast second use: paste a *news headline* and ask:

> "Without doing any research: based only on the phrasing of this headline, what is it *implying*? Which phrasing choices are doing emotional work — 'fears,' 'shocking,' 'why doctors,' 'could'? Don't tell me if it's accurate; I'll check that myself."

Then feed it the abstract and ask:

> "How does the disconnect between this abstract and this headline break down? List each area where the abstract says less than the headline implies."

That's a translation of *drama* back into *data* — a task AIs are genuinely good at, because you've kept the judgment part with yourself.

## A short word on hallucinated studies

When you ask an AI about research, it may invent citations — plausible titles, plausible authors, plausible years, none of them real. This isn't a glitch to be angry about; it's a failure mode to *anticipate*.

The defense is structural, not moral:

1. **Never trust a study title from a chatbot's memory.** Search for it.
2. **Paste in the paper** rather than asking it to recall one. When the source material is in your conversation, invented-citation risk drops sharply, because the model is working from your text, not from memory.
3. **For "what does the evidence say," prefer a real database** — PubMed, Google Scholar — with an AI as your reading companion afterward.

## One worked loop, start to finish

**Input:** *"Study: Omega-3 supplements linked to lower heart-disease risk."*

1. Find an actual abstract (PubMed, search the intervention).
2. Paste it into the AI with the Step 1 prompt.
3. Ask: what design? What's the actual effect size? Absolute or relative? Who was studied?
4. Ask it to quote the sentences supporting its claims.
5. Feed the headline back and ask how the framing drifted.
6. Skim the methods yourself, or run the [Study-Reading Worksheet](07-study-reading-worksheet.html) on it.
7. If the topic touches your own care — bring the question, not the conclusion, to your doctor. (See [Questions for Your Care Team](05-questions-for-your-care-team.html).)

Notice what the AI did in that loop: translation, orientation, contradiction-hunting. What it didn't do: decide anything, assert anything from memory alone, or replace a clinician. That division of labor is the whole trick.

## Warm reminder

You are the auditor; the AI is the interpreter; your doctor is the clinician; and the paper is the evidence. Keep those four jobs in their lanes and this workflow is powerful.

*Next:* the questions worth asking when it's *your* health on the line. → [Questions for Your Care Team](05-questions-for-your-care-team.html)
