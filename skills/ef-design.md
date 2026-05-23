# ef-design

Review a product feature, user flow, or interface through an executive function lens. Identify where EF demands are embedded in the design, and how to reduce them.

## When to use

Call this skill when:
- Designing a new feature or user flow
- Reviewing an existing flow for friction
- Writing copy, instructions, or onboarding content
- Deciding between two design approaches where EF impact is unclear

---

## How to apply this skill

**Step 1.** Read these wiki pages before proceeding. The domain checklist below is a summary — the full intervention tables and failure patterns are in the source pages and will produce a more specific review:
- `wiki/concepts/bdefs-domains.md` — domain definitions and failure modes
- `wiki/strategies/environmental-accommodations.md` — environment-specific patterns
- `wiki/strategies/tech-tools-adhd.md` — digital product patterns

If you cannot read these files, proceed with the checklist below but flag that the review is based on the summary only.

Then read the feature or flow description.

**Step 2.** Walk through each of the five BDEFS domains and check whether the design places a demand on that domain. Use the checklist below.

**Step 3.** Flag each demand found. For each, state: what the demand is, why it creates friction, and the simplest design change that removes it.

**Step 4.** Summarise with a priority order — which changes have the highest impact per effort.

---

## Domain checklist

Source: [[wiki/concepts/bdefs-domains.md]], [[wiki/strategies/environmental-accommodations.md]], [[wiki/strategies/tech-tools-adhd.md]]

### Domain 1 — Time Management
- Does the user need to estimate how long this will take?
- Does the flow have no visible progress indicator?
- Does anything require the user to return at a specific time without an external reminder?
- Does any step have an ambiguous duration ("this might take a while")?

**Design responses:** Progress bars. Time estimates on steps. Built-in reminders rather than expecting the user to set their own. Concrete expected completion times.

### Domain 2 — Organisation
- Does the user need to hold information from a previous step to complete the current one?
- Are there more than 5 items in any list, menu, or decision point?
- Does the user need to locate or gather something before they can proceed?
- Is there any step that requires the user to remember to come back later?

**Design responses:** Persistent context (show what was decided/entered earlier). Progressive disclosure (fewer items visible at once). Single-step flows over multi-session flows. Automatic saves and resumption.

### Domain 3 — Self-Restraint
- Are there high-friction confirmation steps that require the user to pause before acting?
- Is there a risk of impulsive actions (delete, send, publish) with irreversible consequences?
- Does the flow surface tempting distractions (unrelated suggestions, related content, notifications)?

**Design responses:** Undo over confirmation dialogs (undo is lower EF cost). Destructive actions require a deliberate separate step. Distraction-free modes for focus-critical flows.

### Domain 4 — Self-Motivation
- Does the user have to complete a long flow before seeing any result?
- Is there no visible indication of progress toward a meaningful milestone?
- Does the task feel aversive with no proximate reward?
- Is there a long waiting period with nothing actionable?

**Design responses:** Milestone acknowledgements at each step, not just at completion. Progress visibility (X of Y done). Reduce flows to the shortest completable unit. Show immediate value before asking for continued effort.

### Domain 5 — Emotional Regulation
- Does any step involve potential rejection, judgment, or criticism (publishing, sharing, submitting for review)?
- Is there error feedback that is ambiguous, alarming, or shame-inducing?
- Does the user have to evaluate their own work against a standard they might feel they're failing?

**Design responses:** Neutral, specific error messages ("this field requires a number" not "invalid input"). Preview before publish. Draft/private modes that defer social exposure. Normalise partial completion.

---

## Output format

```
EF Design Review: [feature name]

Demands found:
— [Domain]: [specific demand] → [design change]
— [Domain]: [specific demand] → [design change]
...

Priority order:
1. [highest impact change]
2. ...

Clean: [anything the design already handles well]
```

---

## Calibration note

Not every EF demand in a design is a problem. Some friction is intentional (preventing impulsive deletes). The goal is to eliminate **unintentional** EF demands — ones that exist because no one considered EF during design, not because they serve a purpose. When in doubt, ask: "Is this friction here by design, or by default?"
