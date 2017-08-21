# Recursion

#### Loops and Recursion
Recursion makes the solution clearer and there aren't any performance gains.

"Loops may achieve a performance gain for your program. Recursion may achieve a performance gain for your programmer."

#### Stack
A first in last out approach. An example would be plates or sticky notes on top of each other.

Computers use a stack internally called the call stack. Every function call is placed as elements on a stack 
and every time a function is completed and returns, that function call is popped off the stack 
and it returns to the previous function that called it. If you call another function from another function, the 
calling function is paused temporarily until the called function is completed AKA in a partially completed state.

The stack is great because it keeps track of the recursive calls but the cost is that it takes up a lot of memory.
If you have to do a lot of calls, your computer will have to allocate a lot of memory.

There is a concept called tail recursion available in some languages.

#### Exercise:
3.1:  I can see that the greet function was called with the parameter Maggie. And that the greet2 function 
was called from the within the greet function with the parameter Maggie again.

3.2: The program will crash if your recursive calls run forever due to the stack growing. 
Without hitting a base case due to memory issues.