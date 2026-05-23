# ef-triage

Given multiple tasks, options, or decisions, return a single recommendation. No ranked lists. No "it depends." One answer.

## When to use

Call this skill when:
- A user presents more than two things and needs to know what to do next
- A user is asking a choice question and showing signs of decision paralysis
- An agent has surfaced multiple options and needs to collapse them before presenting to the user

## Scope

This skill is for execution-level decisions: what to work on now, which task first, which of these options to pick today. It is not for strategic decisions (which feature to build, which project to pursue long-term) — those require the user's values and cannot be resolved by a priority filter alone. If the list is strategic rather than operational, say so and ask the user to choose rather than applying the filter.

---

## How to apply this skill

**Step 1.** Read the full list of items.

**Step 2.** Apply the priority filter in order — stop at the first filter that produces a clear winner.

**Step 3.** State the recommendation. One item, one sentence of reasoning. Done.

---

## Priority filter (apply in order, stop when resolved)

Source: [[wiki/strategies/interventions-overview.md]], [[wiki/concepts/bdefs-domains.md]] Domain 1 and 4

**Filter 1 — Deadline proximity**
Is anything overdue or due within 2 hours? That item wins. No further reasoning needed.

**Filter 2 — Continuation vs. initiation**
Is anything already in progress (a file is open, partial work exists, a conversation is active)? Prefer continuation. Resuming existing work has lower activation energy than starting fresh — this is not a preference, it is how the initiation system works for EF-impaired users.

Exception: if the same in-progress task has been re-selected in two or more prior sessions without meaningful progress, it is being avoided, not continued. Treat it as avoidant: name it once ("you keep coming back to this without starting it"), give the smallest possible first step, and do not rank it above other items.

**Filter 3 — Smallest activation energy**
Which item has the lowest barrier to starting right now, given the current environment and state? Not the most important — the easiest to begin. EF support is about getting into motion; importance matters after momentum exists.

**Filter 4 — Importance**
If filters 1–3 produce a tie, default to the item with the greatest consequence if not done. This is the only filter that resembles conventional prioritisation.

---

## Output format

One paragraph maximum. Structure:

> Do [specific item]. [One-sentence reason drawn from the filter that resolved it.]

Examples:
> Do the project brief. It's already open and partially written — easier to continue than to start fresh.

> Reply to the client email. It's been 48 hours and waiting longer has compounding consequences.

> Start with the expense report. Everything else requires more setup; this one takes 15 minutes and removes it from the list.

---

## What not to do

- Do not present the reasoning behind multiple filters — pick one and state it
- Do not say "it depends on your priorities" — the user is asking because they cannot currently evaluate priorities
- Do not add qualifiers like "you might also want to consider" — the second thing undoes the first
- Do not rank the full list and let the user pick from the top — ranking is not triage

---

## Edge case: nothing is clearly right

If no filter produces a clear winner and all items are genuinely equivalent, pick the shortest one. Completing anything restores momentum and is worth more than completing the objectively most correct thing at hour two of paralysis.
