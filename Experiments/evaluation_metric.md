# EVALUATION METRIC


## HOW close FROM SOLUTION, name this metric as Progress Score 'P'
- The first metric that comes to my mind, when I thought was,
if n=len(initial string)
and m= len(final string after transitions)
then, 
<Progress score 'P' = (n-m)/n > , gives us a score in (−infinity, 1], where values closer to 1 indicate solutions closer to completion.
- A solved problem has score = 1
- A very bad solution, has where final string is greater than initial, gives negative score.
ex:
string="RAFEISGOOD"
n=10
after transitions, final string ="AF"
m=2
score= (10-2)/10 =0.8

- No worries, for edge cases here.

### Limitations
- Doesn't account for length of source or target, as in some cases only one transition may be remaining for an answer, but that transition in itself may have long src
ex:
for string="RAFEISGOOD"
the final string is "FEISG"
so currently the score is 0.5, 
but the solution was only one transition from solving if a transition
 "FEISG" --> "" 
 existed.

- Sometimes Less Length may not means correctness, as more incorrect transitions removed, giving small final striing, is not what we want.

## To adjust above Score bias for shorter incorrect strings, we introduce Valid Transitions ratio (VTR),

VTR= ( No. of valid transitions applied)/( No. of Proposed transitions)   
Note: We stop on 1st invalid transition

Ex:
String ="ABCFK"
Transitions:
0. "AB"->""
1. "FK" -""
2. "CA" -> ""
3. "C" -> ""
4. "DK"->"C"

Suppose Solution is [1,0,2,4,3]
Proposed transitions: 5

1 is applicable, now str= "ABC"
0 is applicable, now str="C"
2 is not applicable, here we will STOP

Applicable Transitions: 2

therefore, VTR = 2/5 = 0.4

### Edge cases: 
- If solution is empty list=[] (No solution),
meaning no transitions proposed and no invalid transitions.
therefore, we define <VTR=0> as 
No reasoning demonstrated
No progress made.

- If solution is correct, we get VTR=1.

## Limitations
- Does not account to how good a string is reduced (how much progress is made)
Ex:
Two models can have the same VTR but very different outcomes.

Example

Model A: applies 3 valid transitions, reduces string to length 1
Model B: applies 3 valid transitions, reduces string to length 8
Both:
VTR = 3 / 4 = 0.75
But clearly:
Model A reasoned better overall

- A model, may have an invalid transition in middle, but later may recover to give a close solution, but this is not accounted by VTR.


### On broader aspect the Limitations of VTR can be handled by Progress Score and vice versa, 
### Therfore, a final metric can be proposed which is a product of both VTR and Progress score.

# EVALUATION METRIC "m"= P x VTR 
higher the value of m , better the solution.
Max value of m= 1.
Note: A negative value of m indicates that the model’s reasoning expanded the string overall despite partially valid transitions, (will occur upon negative value of P, meaning final string>initial string)


# Let's Test the Metric over few examples:
### Example: Evaluation Metric (m)

**Problem ID:** 001  
**Initial string:** `WPULDXCVQWEBRU`  
**Predicted solution:** `[4, 7, 1, 3]`

---

#### Step-wise execution (brief)

- Apply transition 4 (`WPU → ""`)  
  `WPULDXCVQWEBRU → LDXCVQWEBRU`
- Apply transition 7 (`LDXC → ""`)  
  `LDXCVQWEBRU → VQWEBRU`
- Apply transition 1 (`VQW → ""`)  
  `VQWEBRU → EBRU`
- Apply transition 3 (`EBRU → ""`)  
  `EBRU → ""`

All transitions are valid and the final string is empty.

---

#### Metric computation

- Initial length, `n = 14`
- Final length, `m = 0`

**Progress Score (P):**

P = (n - m) / n = (14 - 0) / 14 = 1


**Valid Transition Ratio (VTR):**
VTR = 4 / 4 = 1

**Final Metric:**
\[
\mathbf{m = P \times VTR = 1 \times 1 = 1}
\]

This represents a fully correct and consistent solution.
