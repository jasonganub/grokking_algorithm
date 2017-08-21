# Selection sort

#### Arrays and Linked Lists
Arrays are contiguous whereas Linked Lists are not.
 
Arrays are great for reading random elements whereas Linked Lists require traversing through every element.

Linked Lists however allow inserts to be very simple without shifting other elements (very scalable). The same goes for 
deletion since you can change the previous element to point to another element instead.

#### Runtime complexities:
Arrays:
* Read: O(1)
* Insertion: O(n)
* Deletion: O(n)

Linked Lists:
* Read: O(n)
* Insertion: O(1)
* Deletion: O(1)

O(n) is linear time
O(1) is constant time

#### Exercise:
2.1: Linked List since there are many insertions and few reads. 

2.2: Linked List because every time an order is popped from the top of the list, all of the following elements 
will need to be shifted which is very inefficient.
 
2.3: Array because even though it's a binary search searching for usernames on Facebook, it requires random access 
to get the mid value everytime.

2.4: The downside of using an array for inserts is that every time you insert an element or username in this case 
to the beginning of the array, it will take n times to shift all of the other users to the right. When adding new users 
to an array, every following element shifts to the right.

2.5: For searching, it is slower than arrays but the same time as Linked Lists since it requires traversal. 
For inserting, it is faster than arrays but the same amount of time as Linked Lists. This is a hybrid model of 
having an array of Linked Lists. Note to self, I may have heard about this before as a way to avoid collissions for 
Hash Tables by inserting a Linked List inside of the value of a Hash Table.