# Sed-Style String Rewriting with LLMs
---

## 1. Project Overview

This project studies how Large Language Models (LLMs) reason over **sed-style string rewriting puzzles**, where an initial string must be reduced to the empty string using a set of rewrite transitions. Each transition replaces *all* occurrences of a source substring with a target substring.

The primary goal of this work is  to understand:

* how different prompting strategies affect LLM reasoning,
* where LLMs fail or succeed,
* and how to evaluate partial progress meaningfully when full solutions are not found.
* How humans behaviour vary in terms of solving

---

## 2. What I Did / Did Not Do

### What I Did
- > **ALL 3 Tasks and Bonus Task Done**

* Designed and generated a **custom dataset** of solvable string-rewriting puzzles (100 records). 
* Added **manually curated adversarial puzzles** to expose reasoning failures (10 records).
- (**See src for dataset code and data for dataset**)

* Evaluated multiple prompting strategies:
  * Zero-shot
  * Few-shot
  * Chain-of-Thought (CoT)
  * Creative constraint-aware prompting (CASV) - (The Creative One)
- (**See .md files of Experiments folder for insights, and Results folder, for experimental results**)

* Benchmarked primarily across **2 LLMs** (Gemini Web, GPT Go).

* Designed **custom evaluation metrics** beyond binary accuracy.
* Conducted a **Man vs Machine** qualitative comparison.
- (**See ANALYSIS folder for above two**)



### What I Did Not Do

* I did not use APIs (all experiments were done via web interfaces,as through it, I have closely observed model behavior, and avoided API rate limits or setup overhead).

---

## 3. Dataset Construction

Dataset details are documented in `data/README.md`.

### Summary
* Total puzzles: **110**
  * 100 auto-generated
  * 10 manually curated (adversarial, overlapping)
* Difficulty levels:

  * Easy: 2–3 transitions, non-overlapping
  * Medium: 4–7 transitions
  * Hard:  >7 transitions
  * Hard (manual): overlapping transitions, adversarial ordering

### Design Rationale

* Puzzles are **reverse-constructed** from valid deletion sequences to guarantee solvability.
* Transitions are shuffled to avoid greedy solutions.
* Distractor transitions introduce loops and dead ends, forcing global reasoning.

---

## 4. Prompting Strategies Evaluated

All prompting experiments are documented in the `experiments/` directory.

### 4.1 Zero-shot Prompting

* Directly asks the model to find any valid transition sequence.
* Performs well on easy and most medium puzzles.
* Fails consistently on manually curated hard puzzles.

### 4.2 Few-shot Prompting

* Provides a solved example before the target puzzle.
* Improves performance on medium puzzles.
* Still unreliable on hard puzzles; behavior is model-dependent.

### 4.3 Chain-of-Thought (CoT) Prompting

* Explicit step-by-step reasoning with state tracking.
* Reduces hallucination and random guessing.
* Still does not solve adversarial puzzles.

### 4.4 Creative Prompting: Constraint-Aware State Verification (CASV) 

* Models are forced to enumerate applicable transitions at each step.
* Significantly improves performance on hard puzzles **for Gemini**.
* GPT models struggled to benefit from the same constraints.

| Method    | # Runs | Rationale                           |
| --------- | ------ | ----------------------------------- |
| Zero-shot | 10     | Establish baseline distribution     |
| Few-shot  | 5      | Measure relative improvement        |
| CoT       | 3      | Qualitative reasoning analysis      |
| CASV      | 3      | Constraint aware state verification |
---

## 5. Evaluation Metrics

Evaluation Metric "m" is designed as product of:

### 5.1 Progress Score (P)

Measures how close the model gets to the solution:
P = (n-m)/n
where:

* `n` = initial string length
* `m` = final string length

Range: (−∞, 1], where 1 indicates a solved puzzle.

### 5.2 Valid Transition Ratio (VTR)

Measures reasoning discipline:
VTR = No. of valid transitions applied/ No. of proposed transitions
- Execution stops at the **first invalid transition**.

### Therefore, 
m = P x VTR


This balances **progress** and **logical consistency**.
Negative values indicate net harmful reasoning (string expansion).

Worked examples are provided in `experiments/evaluation_metric.md`.

---

## 6. Man vs Machine

A qualitative comparison was performed by giving puzzles to human solvers (friends and family) and comparing solving behaviour and outcomes with LLMs.

### Key Findings
* Humans are generally better at thinking ahead, keeping the overall goal in mind, and knowing when not to delete something too early.
* LLMs are very good at spotting patterns in the string and applying rewrite rules quickly and consistently.
* Many of the manually designed hard puzzles could be solved by humans in about 5–10 minutes, but LLMs often failed on them.
* On the other hand, the auto-generated puzzles were solved very quickly by LLMs, while humans too solved them but required few minutes.

This analysis is documented in `experiments/man_vs_machine.md`.

---

## 7. Reproducibility

* All puzzles are stored in JSON format.
* Prompts are explicitly documented.
* Results are logged per puzzle with failure reasons.
* Experiments can be inspected manually without compute-heavy dependencies.

---

## 8. Limitations and Future Work

* No backtracking or search-based solvers were implemented.
* Larger-scale experiments were limited by compute and time.
* Future work could explore:

  * classical planning baselines,
  * learned heuristics,
  * hybrid human–LLM strategies,
  * or symbolic solvers for comparison.


---

## Final Note

This project ensures **rigor, transparency, and analysis** over raw performance.
Failures are documented, as they reveal meaningful insights into LLM reasoning behavior.