# Lychrel_number
Iterative process of adding numbers with their palindrome in order to end up with a new palindrome, or not... (Lychrel number).

## What does the algorithm do ?
- x is an integer positive number
- We add this number with its palindrome (its mirror).
- If the result is a palindrome, the iteration process stops
- If the result is not a palindrome, we add this result with its palindrome. This iterative process is repeated as long as the 
result is not a palindrome.
- The function returns a list containing the intermediate calculation steps until obtaining the palindrome
- By default (`detailed = False`), only the result of intermediate operations is added to the list, but a more detailed display of the 
calculations is possible by setting `detailed = True`, in this case, each addition and its result appear in lists.

Exemple for 192 : 192+291 = 483 | 483+384 = 867 | 867+768 = 1635 | 1635+5361 = 6996
- `detailed = False` : [483, 867, 1635, 6996]
- `detailed = True` : [[192, 291, 483], [483, 384, 867], [867, 768, 1635], [1635, 5361, 6996]]

![cap_192](https://user-images.githubusercontent.com/11463619/98821956-7da61a80-2430-11eb-96a6-a1c6d148444f.png)

## What's a Lychrel number ?
There are some numbers for which this iterative process does not end, i.e. the algorithm cannot result in a palindrome in a 
reasonable time. 196 is on of them, for this value supercomputers reached 1 billion-digit numbers without reaching the palindrome, 
these numbers are called Lychrel numbers. There are other numbers like this: 295, 394, 493, 592, 689 ...

In this algorithm, in order to avoid endless loops, a duration in seconds is allocated to the calculation, beyond this allotted 
time the process stops, meaning that the number inserted is potentially a Lychrel number. By default the allotted time is `wd = 5`, 
i.e. 5 seconds. 
When the iteration stops due to time out, the function returns a list in which is found :
- [0] "ITER. STOP" flag
- [1] Time allocated to the calculation (in seconds)
- [2] Value on which the iteration process stopped (scientific notation)
- [3] The initial number inserted

![cap_lychrel](https://user-images.githubusercontent.com/11463619/98821963-7f6fde00-2430-11eb-8e8d-bd5fe3b0c36a.png)

## An unsolved problem
