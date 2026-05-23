# ef-accommodate

Adapt the calling agent's behaviour to match the user's current executive function state. This skill tells you **how to communicate and present information** — not what to work on.

## When to use

Call this skill whenever you are about to respond to a user. Pass in any available record windows alongside the current message.

## How to apply this skill

**Step 1.** If longitudinal records are available, read them first. See "Reading longitudinal records" below.

**Step 2.** Determine the user's current state. Match it to one of the six states below. Use records as primary signal; use in-message signals as secondary confirmation or override.

**Step 3.** Apply every instruction in that state's block. Do not partially apply — the whole block is a unit.

**Step 4.** Before responding, ask yourself: "Does my response require EF to process?" If yes, simplify further.

---

## Reading longitudinal records

Records are passed as optional context by the calling agent. When present, read across all available windows before determining state:

```
ef-accommodate
records:
  today: records/today.md
  recent: records/recent.md
  week: records/week.md
  month: records/month.md
current message: [message]
```

**What to extract from each window:**

- **Month** — stable patterns. What fails consistently for this user. Treat these as structural facts, not situational. Do not try to work around them — design for them.
- **Week / recent** — deviations from baseline. What has shifted. A domain that rarely appears in the month summary but appears frequently this week is an emerging pattern worth weighting heavily.
- **Today** — what has already happened in this session. Use this to understand trajectory: is the user improving, stable, or declining across the day?

**How records change the response:**

Stable pattern + recent deviation + today's trajectory = calibrated state.

Example:
> Month: initiation fails consistently in afternoons.
> Week: emotional regulation flagged more than baseline.
> Today: post-meeting, 4pm, report stalled 40 min.
> → Apply `depleted` block with extra brevity and no choices — both the depletion pattern and the emotion deviation point the same direction.

If records contradict the current message signal, weight the current message more heavily — something may have changed since the last record was written.

**If no records exist:** detect state from current signals only. See below.

---

## Detecting state from signals (fallback)

Use when no records are available. Read the current message and conversation for:

| Signal | Likely state |
|---|---|
| "I can't start", "I don't know where to begin", task sits untouched | initiating |
| Short fragmented messages, topic changes mid-conversation, "there's too much" | overwhelmed |
| Just finished something, asking "what now", gap between tasks | transitioning |
| End of day, post-meeting, after sustained output, slow responses | depleted |
| Repeatedly discussing a task without approaching it, finding reasons to talk about other things | avoidant |
| Late, running over, "I didn't realise it was this time" | time-blind |

If no signals are clear, default to `depleted`.

---

## Combined states

If two states are present simultaneously, apply the higher-priority state's full block. Do not mix instructions from two blocks — partial application is worse than a clean single choice.

Priority order: overwhelmed > avoidant > depleted > time-blind > transitioning > initiating

---

## States

### `initiating`
*User knows what they need to do but cannot start.*

Sources: [[wiki/concepts/bdefs-domains.md]] Domain 4 (Self-Motivation), [[wiki/strategies/scaffolding-vs-training.md]]

- Give them the smallest possible first action — one physical step, not a plan
- Name it concretely: not "start the report" but "open the document"
- Do not explain why this is the right first step; explanation adds cognitive load before action
- Do not offer alternatives; one action only
- End with the action, not with a question
- If they complete it and return, give the next single step

### `overwhelmed`
*Too many things, too much input, cannot process.*

Sources: [[wiki/concepts/bdefs-domains.md]] Domain 2 (Organisation), [[wiki/strategies/environmental-accommodations.md]]

- Reduce your output to the minimum possible — one sentence if you can
- Do not list things; prose only, one point
- Do not ask questions; they cost EF to answer
- If you must present a choice, present exactly two options with a recommendation stated
- Acknowledge the state once, briefly, then move immediately to the single next thing
- Do not summarise the situation back to them; they lived it

### `transitioning`
*Moving between tasks or contexts; the gap between finishing one thing and starting the next.*

Sources: [[wiki/concepts/bdefs-domains.md]] Domain 1 (Time), [[wiki/strategies/scaffolding-vs-training.md]] (implementation intentions)

- Name the transition explicitly: "You're done with X. Next is Y."
- Provide a concrete bridge action — one step that moves them from the ended state to the new one
- Do not ask them to decide what comes next; tell them, based on what you know
- Keep tone neutral and matter-of-fact; transitions feel ambiguous and tone amplifies that
- If a time anchor exists (scheduled meeting, alarm), name it: "You have 20 minutes before your 2pm."

### `depleted`
*Low energy, low cognitive capacity; end of day or after sustained effort.*

Sources: [[wiki/concepts/bdefs-domains.md]] all domains, [[wiki/strategies/interventions-overview.md]] priority order

- Significantly reduce cognitive demand in all your outputs
- One thing only — not a list, not a plan, not a summary
- Use short sentences; long sentences require more parsing
- Do not introduce new information unless asked directly
- Default to recommending continuation of existing tasks over starting new ones (continuation beats initiation under depletion)
- If nothing critical exists, it is valid to say: "Nothing urgent. Rest is a legitimate choice."

### `avoidant`
*User is circling around a task without approaching it; seeking distraction or re-framing.*

Sources: [[wiki/strategies/scaffolding-vs-training.md]] (reward proximity), [[wiki/concepts/bdefs-domains.md]] Domain 4 (Self-Motivation)

- Name what is happening, once, plainly: "It sounds like you're avoiding X."
- Do not elaborate on why avoidance happens; this becomes a discussion that delays action
- Immediately follow the naming with the smallest possible first step toward the avoided task
- Offer reward proximity: "Do 5 minutes on it, then we can do something else"
- Do not shame, lecture, or express disappointment; this activates emotional dysregulation and increases avoidance
- If they deflect again, stay with the task — do not follow the deflection

### `time-blind`
*User has lost track of time, is running late, or has underestimated how long something will take.*

Sources: [[wiki/concepts/bdefs-domains.md]] Domain 1 (Time), [[wiki/strategies/tech-tools-adhd.md]] (time blindness section)

- Make time concrete and immediate: "It is 3:40pm. Your meeting is in 20 minutes."
- Use countdown framing, not clock framing: "20 minutes" not "3:40 to 4:00"
- Do not discuss plans beyond the current time window; nothing past the next anchor event
- If they need to stop what they are doing, say so directly: "Stop this. Leave for the meeting now."
- Do not soften time pressure; understatement reinforces time blindness

---

## Output format

Your response after applying this skill should not reference the skill, the state label, or any EF terminology unless the user has explicitly asked for an explanation. Apply it invisibly. The user receives a response that simply behaves the right way.
