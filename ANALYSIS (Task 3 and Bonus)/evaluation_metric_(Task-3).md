# EVALUATION METRIC


#### HOW close FROM SOLUTION, name this metric as Progress Score 'P'
- The first metric that comes to my mind, when I thought was,
if n=len(initial string)
and m= len(final string after transitions)
then, 
* **Progress score 'P' = (n-m)/n** , gives us a score in (−infinity, 1], where values closer to 1 indicate solutions closer to completion.
  - A solved problem has score = 1
  - A very bad solution, has where final string is greater than initial, gives negative score.
* ex:<br>
string="RAFEISGOOD"  <br>
n=10  <br>
after transitions, final string ="AF"  <br>
m=2  <br>
score= (10-2)/10 =0.8  <br>

- No worries, for edge cases here.

### Limitations
- Doesn't account for length of source or target, as in some cases only one transition may be remaining for an answer, but that transition in itself may have long src
ex:<br>
for string="RAFEISGOOD"<br>
the final string is "FEISG"<br>
so currently the score is 0.5, <br>
but the solution was only one transition from solving if a transition<br>
 "FEISG" --> "" <br>
 existed.

- Sometimes Less Length may not means correctness, as more incorrect transitions removed, giving small final striing, is not what we want.

## To adjust above Score bias for shorter incorrect strings, we introduce Valid Transitions ratio (VTR),

VTR= ( No. of valid transitions applied)/( No. of Proposed transitions)   <br>
Note: We stop on 1st invalid transition<br>

Ex:<br>
String ="ABCFK" <br>
Transitions:
0. "AB"->""
1. "FK" -""
2. "CA" -> ""
3. "C" -> ""
4. "DK"->"C"


Suppose Solution is [1,0,2,4,3]<br>
Proposed transitions: 5


1 is applicable, now str= "ABC" <br>
0 is applicable, now str="C"<br>
2 is not applicable, here we will STOP<br>

Applicable Transitions: 2<br>

therefore, VTR = 2/5 = 0.4<br>

### Edge cases: 
- If solution is empty list=[] (No solution),
meaning no transitions proposed and no invalid transitions.
therefore, we define **VTR=0** as <br>
No reasoning demonstrated <br>
No progress made.

- If solution is correct, we get VTR=1.

## Limitations
- Does not account to how good a string is reduced (how much progress is made)<br>
Ex:<br>
Two models can have the same VTR but very different outcomes.


Example<br>

Model A: applies 3 valid transitions, reduces string to length 1<br>
Model B: applies 3 valid transitions, reduces string to length 8<br>
Both:<br>
VTR = 3 / 4 = 0.75<br>
But clearly:<br>
Model A reasoned better overall<br>

- A model, may have an invalid transition in middle, but later may recover to give a close solution, but this is not accounted by VTR.


#### On broader aspect the Limitations of VTR can be handled by Progress Score and vice versa, <br>
#### Therfore, a final metric can be proposed which is a product of both VTR and Progress score.

# EVALUATION METRIC "m"= P x VTR 
higher the value of m , better the solution.<br>
Max value of m= 1.<br>
Note: A negative value of m indicates that the model’s reasoning expanded the string overall despite partially valid transitions, (will occur upon negative value of P, meaning final string>initial string)


# Let's Test the Metric over few examples:

### Example1 (Zero Shot): 
Problem ID: 001  
Initial string: `WPULDXCVQWEBRU`  
Predicted solution: `[4, 7, 1, 3]`

All transitions are valid and the final string is empty.
---
#### Metric computation
- Initial length, `n = 14`
- Final length, `m = 0`
Progress Score (P):
P = (n - m) / n = (14 - 0) / 14 = 1

Valid Transition Ratio (VTR):
VTR = 4 / 4 = 1

Final Metric:
m= P x VTR =1x1=1

This represents a fully correct and consistent solution.

---------------------------------------------
### Example 2 (Few Shot):
Problem ID: H03  
Initial string: `XATCFLMODKF`  
Predicted solution: `[6, 1, 5, 0]`

Execution stops at transition `5` since it is not applicable.  
Final string obtained: `AKTB`
---
#### Metric computation
- Initial length, `n = 11`
- Final length, `m = 4`

Progress Score (P):  
P = (n - m) / n = (11 - 4) / 11 ≈ 0.64

Valid Transition Ratio (VTR):  
Valid transitions before failure = 2  
Proposed transitions = 4  

VTR = 2 / 4 = 0.5

Final Metric:  
m = P x VTR ≈ 0.64 x 0.5 ≈ 0.32

This represents partial progress with an early reasoning failure.
-------------------------------------------------

### Example 3 (Chain of Thought):
Problem ID: H07  
Initial string: `LKFTNTBOORK`  
Predicted solution: `[1, 0, 2, 14, 9]`

All proposed transitions are valid, but the final string is non-empty.  
Final string obtained: `K`
---
#### Metric computation
- Initial length, `n = 11`
- Final length, `m = 1`

Progress Score (P):  
P = (n - m) / n = (11 - 1) / 11 ≈ 0.91

Valid Transition Ratio (VTR):  
Valid transitions = 5  
Proposed transitions = 5  

VTR = 5 / 5 = 1

Final Metric:  
m = P x VTR ≈ 0.91 x 1 ≈ 0.91

This represents a near-complete solution with correct reasoning but incomplete termination.

--------------------------------------------------------
### Example 4 :
Problem ID: H09  
Initial string: `RAFEISGOOD`  
Predicted solution: `[1, 2, 3, 5, 6, 0, 0]`

Execution stops at the first occurrence of transition `0`, which is not
applicable at that point.  
Final string obtained: `F`
---
#### Metric computation
- Initial length, `n = 10`
- Final length, `m = 1`

Progress Score (P):  
P = (n - m) / n = (10 - 1) / 10 = 0.9

Valid Transition Ratio (VTR):  
Valid transitions before failure = 6  
Proposed transitions = 7  

VTR = 6 / 7 ≈ 0.86

Final Metric:  
m = P x VTR ≈ 0.9 x 0.86 ≈ 0.77

This represents strong progress with disciplined reasoning, but failure
due to an invalid late-stage transition.


#### As we have seen the four examples, we get a score out of 1, which  tells about how well the solution is.
#### Upon manual analysis over the above examples, we see the metric have done a good job in labeling a score for solutions reaching closer to the answer.  