# Chain-of-Thought Prompting
### Too Long? (Read Key Insight at the bottom to get an idea)

## Prompt Used
The model was explicitly instructed to reason step-by-step, track the current string after each transition, and avoid applying transitions whose preconditions were not satisfied.

- The exact prompt given was:
You are given a string rewriting puzzle.

Initial string:

<INITIAL_STRING>

Transitions (indexed):
0: src -> tgt
1: src -> tgt
2: src -> tgt
...

Task:
Find a sequence of transitions that reduces the initial string to the empty string.

Instructions:

- Think step by step.
- After each transition, explicitly write the current string.
- Do not apply a transition unless its src is present in the current string.
- If no valid transition applies, state that clearly.
- At the end, output only the final solution in this JSON format:
{
  "solution": [index1, index2, ...]
}
---------------

## Expected Effect
Explicit reasoning is expected to improve state tracking and reduce
invalid transition application compared to zero-shot and few-shot prompting.

---

## Experimental Setup
Chain-of-Thought prompting was evaluated on:
- 1 medium puzzle (auto-generated)
- 2 hard puzzles (manually curated, adversarial)

Each puzzle was attempted once per model (Gemini web and GPT web).

---

## Quantitative Results

| Difficulty | Solved | Total |
|----------|--------|-------|
| Medium   | 1      | 1     |
| Hard    | 0      | 2     |

---

## Observations

- CoT prompting successfully solves medium puzzles that require
  moderate planning depth.
- Compared to zero-shot and few-shot prompting, CoT reduces random guessing and long hallucinated solution sequences, this time it reaches the solution more closely as in case of H07.
- Models stop early and admit uncertainty when
  reasoning step-by-step as seen in H08.
- Despite explicit reasoning and more time taken by the LLM, CoT could not solve hard problems.

---

## Failure Modes

The dominant failure modes under CoT prompting include:
- Applying transitions which were not applicable.
- Reaching terminal non-empty strings with no applicable transitions.
- Incorrectly concluding that no solution exists for solvable puzzles.
(The 2nd and 3rd were not seen was not seen in prev prompting experiments)

---

## Key Insight
Solved medium, but couldn't solve hard puzzles.
Chain-of-Thought prompting improves reasoning discipline and reduces hallucination and reaches the solution closesly but could not resolve global planning and backtracking for adversarial string rewriting tasks.
