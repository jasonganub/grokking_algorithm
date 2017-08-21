# Quicksort

#### Divide and Conquer (D&C)
Divide and Conquer are recursive algorithms. 
1) Figure out a simple case as the base case.
2) Figure out how to reduce your problem and get the base case.

Ask yourself if you can solve this problem using divide and conquer?

When writing a recursive function involving an array, the base case is often an empty array or an array 
with one element.

Why do this recursively if I can do it easily with a loop?
For one, it is easier to read and more concise.
Second, functional programming languages like Haskell don't have loops so recursive solutions are required.

#### Exercise:
4.1: I wrote the sum function in the sum.py file.

4.2: I wrote the count function in the count_items.py file.

4.3: I wrote the max function in the max_num.py file.

4.4: For a binary search, the base case is when the array has a length of 1. If the value you're seeking 
is the item in the array, you found it. Otherwise, it's not in the array.

The recursive case is to mid value is less than the one you're seeking, then set the new left
value to the mid point + 1 (shift right one). If it's greater, than shift the new right value 
to the mid point - 1 (shift left). Basically, you are throwing away one half of the array every time.