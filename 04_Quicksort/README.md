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

Quick sort uses a pivot to sort elements less than the pivot value to the left and 
elements greater than the pivot to the right. In the end, the sorted result is 
the left sub-array + the pivot + the right sub-array.

The runtime of quick sort is O(n log n) in the best case and O(n^2) in the worst case. It 
all depends on where the pivot lands.

Merge sort is also O(n log n) but O(n log n) is the average case.

Big O notation of O(n) really means c * n.
C is the constant, some fixed amount of time that your algorithm takes.

However; constants are usually ignored because if two algorithms have different Big O times, 
then the constants don't matter.

However; sometimes the constant can make a difference. Quicksort has a smaller constant than 
merge sort. They're both O(n log n) but quick sort is faster in practice because it hits the average 
case more often than the worst case.

It is considered O(n log n). N is from checking each item in the array to see if it is lesser or greater than 
the pivot point. The next part is tricky. The solution doesn't know whether the array is already sorted or not.
If it happens to already be sorted and you keep using the pivot point at index 0, you'll never have a lesser than 
sub-array and will only have a large greater than sub-array. This is very inefficient and you will call the recursive 
call stack n times.

However; if you chose the middle or a random pivot point. You reduce the chance of having an unbalanced lesser and 
greater than sub-array. A balanced lesser and greater than sub-array means you will make less recursive calls since 
they are already divided and half the size. This is how you get log n since it is a divide and conquer method.

In the best case scenario, this results in O(n) * O(log n) = O(n log n)
In the worst case scenario, this results in O(n) * O(n) = O(n^2)

The best case for quick sort happens to also be the average case. 
Instead of picking the first item as the pivot point, pick a random element in the array and it will complete 
in O(n log n) time on average. It's one of the fastest sorting algorithms out there and a great example of 
divide and conquer.

#### Exercise:
4.1: I wrote the sum function in the sum.py file.

4.2: I wrote the count function in the count_items.py file.

4.3: I wrote the max function in the max_num.py file.

4.4: For a binary search, the base case is when the array has a length of 1. If the value you're seeking 
is the item in the array, you found it. Otherwise, it's not in the array.

The recursive case is to mid value is less than the one you're seeking, then set the new left
value to the mid point + 1 (shift right one). If it's greater, than shift the new right value 
to the mid point - 1 (shift left). Basically, you are throwing away one half of the array every time.

4.5: O(n)

4.6: O(n)

4.7: O(1)

4.8: O(n^2)