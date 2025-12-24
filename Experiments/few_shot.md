
# Zero-shot Prompting
### Too Long? (Read Key Insight at the bottom to get an idea)

## Prompt Used
The model was given the puzzle description and an example solution for another problem, and  asked to find any valid sequence of transitions that reduces the initial string to empty.

### The exact prompt given was: 
You are given string rewriting puzzles.

Each puzzle has:
- an initial string
- a list of indexed transitions
Each transition replaces ALL occurrences of src with tgt.

--- Example ---

Initial string:
PFASFX <for examople>

Transitions (indexed):
0: FX -> ""
1: PF -> ""
2: AS -> ""

One valid solution is:
[2, 1, 0]

--- New Puzzle ---

Initial string:
<NEW_INITIAL_STRING>

Transitions (indexed):
0: ...
1: ...
2: ...
...

Your task:
Return ANY sequence of transition indices that reduces the initial string
to an empty string.

Rules:
- Transitions can be reused.
- The goal is not to minimize steps.
- Return only a JSON object in this format:

{
  "solution": [index1, index2, ...]
}

----------------------------
## Expected Effect
Providing an example is expected to improve state tracking and
transition ordering compared to zero-shot prompting.

## Experimental Setup
Evaluated few-shot prompting on:
- 2 medium puzzles (auto-generated)
- 3 hard puzzles (manually curated)
- Not easy, because already zero shot gave us correct results

Each puzzle was attempted exactly once.
Also prompts were given to both Gemini-3 and GPT-GO, but was explicitly recorded when there was a different answerc(seen in hard puzzles)
---

## Quantitative Results

| Difficulty | Solved | Total |
|----------|--------|-------|
| Medium   | 2      | 2     |
| Hard    | 1      | 6     |

- Hard ones's in detail

| Puzzle | Model    | Solved? | Failure type                |
| ------ | -------- | ------- | --------------------------- |
| H02    | Gemini-3 | No       | Invalid transition          |
| H02    | GPT Go   | Yes      | solved after taking time    |
| H04    | Gemini-3 | No       | Invalid transition          |
| H04    | GPT Go   | No       | Invalid transition          |
| H07    | Gemini-3 | No       | Invalid transition          |
| H07    | GPT Go   | No       | Invalid transition          |

---

## Observations

- Few-shot prompting had improved performance on medium puzzles.
- Compared to zero-shot, the model is less likely to choose obviously invalid early transitions on medium instances.
- On hard puzzles, few-shot prompting does not reliably prevent invalid transition application or loss of state consistency.
- Different models exhibit different behaviors under the same few-shot
  prompt: GPT occasionally succeeds where Gemini fails, but both could not solve most of hard puzzles.

---

## Failure Modes

Common failure modes under few-shot prompting include:
- Applying transitions whose preconditions were invalidated by earlier steps.
- Hallucinating applicability of transitions that do not occur in thecurrent string.
- Reaching terminal non-empty strings with no applicable transitions,
  indicating global planning failures.



---

## Key Insight

Few-shot prompting provides a strong inductive bias for simpler puzzles, the medium puzzle failed in zero shot, was solved in few shot, 1 hard puzzle was solved by GPT which gemini could not, other than that all other puzzles were not solved correctly.