# ef-scaffold

Break down any task or goal into an EF-aware action sequence — the minimum number of steps, with the lowest-friction entry point, and no ambiguity in what to do next.

## When to use

Call this skill when:
- A user needs to start something and the task feels too large or undefined
- An agent needs to plan a feature or piece of work with EF friction in mind
- A task has been started and stalled, and re-entry is needed

## How to apply this skill

**Step 1.** Read the task description. Identify which BDEFS domains are most at risk of causing failure for this task type.

**Step 2.** Apply the decomposition rules below.

**Step 3.** Check the output against the anti-patterns. If any apply, revise.

**Step 4.** If ef-accommodate has already been applied in this session, filter your output through that state's constraints before delivering it. A `depleted` accommodation means deliver only the first step of the scaffold, not the full breakdown. The accommodation sets the container; the scaffold fills it.

---

## Domain-specific failure patterns to check

Read [[wiki/concepts/bdefs-domains.md]] for the full domain descriptions. For scaffolding purposes:

| Domain at risk | Failure sign in the task | Scaffold adjustment |
|---|---|---|
| Time (Domain 1) | Deadline exists, or task has no fixed duration | Add time estimate + buffer (×1.5). Name the first time anchor. |
| Organisation (Domain 2) | Multi-step, or outcome requires holding prior steps in mind | Write every step externally. Sequence explicitly. No implicit "then do the obvious thing." |
| Self-Motivation (Domain 4) | Task is aversive, long, or has no immediate reward | Reduce to 5-minute unit. Attach a reward to step 1 completion, not task completion. |
| Emotion (Domain 5) | Task involves rejection risk, criticism, or social exposure | Name that this step might feel uncomfortable. Give a concrete post-step recovery action. |

---

## Decomposition rules

Source: [[wiki/strategies/scaffolding-vs-training.md]] (hierarchical task decomposition, implementation intentions)

**Rule 1 — One initiating action**
The first step must be completable in under 2 minutes with no prerequisites. It is a physical action: open, write, call, go to. Not: "plan", "think about", "figure out".

**Rule 2 — No step depends on a prior step being held in memory**
Every step must be independently readable and actionable. A reader who has not seen step 1 must be able to execute step 2 from its description alone.

**Rule 3 — Eliminate optionality**
Do not write "you could do X or Y". Write "do X". If a decision is genuinely required, make it explicit as its own step with a recommendation.

**Rule 4 — Minimum viable sequence**
Three tiers, but only as deep as needed:
- **Goal** — what done looks like (one sentence)
- **Steps** — discrete, ordered actions (2–6 usually; never more than 8)
- **First step** — isolated, with implementation intention format: "When [trigger/time/place], I will [specific action]"

**Rule 5 — Time estimates on each step**
Every step gets a realistic duration. Add 50% to any estimate for tasks in the time management domain (time blindness means underestimation is systematic, not occasional).

---

## Output format

```
Goal: [one sentence — what done looks like]

Steps:
1. [action] (~Xmin)
2. [action] (~Xmin)
...

Start here: When [specific trigger], [first physical action].
```

Do not include rationale, EF terminology, or explanations of why steps are ordered this way unless the user asks. The scaffold should be immediately usable without reading overhead.

---

## Anti-patterns to eliminate before output

- "Think about what you need" — not a step
- "Gather the relevant materials" — too vague; name them
- "Work on the first section" — not bounded; add a time or output target
- Lists longer than 8 steps — decompose into sub-projects instead
- Steps that begin with "Make sure" — rewrite as a specific action
- Any step containing "etc." — close the open end or delete it
