# MAN Vs MACHINE

The primary aim of this task is to analyze qualitative differences between human and LLM reasoning on string-rewriting puzzles.

### SETUP
- After carrying out the previous tasks, I had given puzzles to my friends and family members, (even kept on socials) and asked them to solve and if done, give the time, and where they felt difficulty. The overall results were mostly as expected.

## Problems Easy for Humans but Difficult for LLMs

Several manually curated hard puzzles (e.g., H04, H10, H09) were found to be solvable by humans in about 5-10 minutes, and auto generated easy and medium problems, were solved easily in 1-2 minutes, whereas we have seen that most manually curated hard puzzles were consistently challenging for LLMs. Though it answered even hard puzzles in about 30 seconds, maximum it took was 2 minutes. 

Human solvers typically reason globally. Many instinctively mentally track which substrings must be preserved for
future transitions.
Some worked backward  from the
empty string after not being able to solve by forward substituting. 
In contrast, LLMs frequently commit to locally
attractive deletions that invalidate later steps. Even under Chain-of-Thought and constraint-aware prompting, models struggle to recover once an early mistake is made.
Even after letting know, to check applicability at each stage in case of CASV (constraint-aware state-verification) prompting, in one case same mistake was seen.



## Problems Easy for LLMs but Difficult for Humans

Code-generated easy and medium puzzles exhibit a bit contrasting behaviour.
These puzzles, though does not have overlapping transitions, but have long similar independent deletions (similar src-> different tgt).
LLMs solve such instances reliably, even in zero-shot settings, due to strong pattern-matching abilities. The anwer is generated within 5-10 seconds in zero shot and few prompt, 
whereas in COT and CASV, it takes time to check or verify at each stage, still under 20 seconds at max.

Human solvers too easily solve these problems, however, must manually scan for multiple occurrences of same source of transition especially as string length increases.

- Note, a good number of people (too gave up) could not solve some extremely hard long overlapping hard problems, which were manually curated, and we have seen CASV prompting on Gemini especially, able to solve some of them.

## Key Insight

Though there has been a division between humans and machines in terms of time and reliability over easy and hard problems respectively, No definitive conclusion can be drawn that extremely hard puzzles are solvable only by humans and not by machines.
 Observations suggest a  distinction of strengths like:
 - humans excel at long-horizon, global state planning and invariant preservation.
 - LLMs perform well on tasks dominated by local and linear pattern matching. 
Adversarial puzzle design exposes this gap, highlighting few differences between human reasoning and current LLM behavior