# Hash Tables

#### Hash Tables vs Arrays
Hash tables are great for storing associated or mapped values. A Hash table is an array that consists 
of a key and value pair. It's basically a combination of a hash function and an array.

Hash functions are built in and they take the key and convert it to an integer which will be the index of 
the array that will store your value. Hash tables when reading are a constant speed of 1 which is instantaneous.

Compared to a regular array, if you knew what you are searching for, you would have to loop n times in the array 
to check if each item is the value you're searching for. However; a hash table will take your key, hash it, and then 
get the value from the index.

#### Examples
A good example of a real world use of hash tables would be a phone book that contains a name and number.

Hash tables are also used for caching. When receiving a request or url, companies will implement a way to hash the 
data or returned page and insert it into the hash table. When requested again with the same url, it will return it 
quickly which saves both the load on the backend as well as a quicker response for the user. If the request is new, 
return it to the user as well as inserting it into the hash table.

#### Recap
* Modeling relationships between two things.
* Filtering out duplicates.
* Caching/memorizing data instead of re-running or re-rendering.

#### Collisions
Rare but there can be collisions for two values to fight over the same key location. This can be dealt with by 
inserting a linked list at that slot. 

It's not that big of a deal to have a linked list since it's rare enough to have collisions which means 
you will have very few values in the linked list.

A load factor is the amount if items divided by the amount of slots available in the hash table array.
If it runs out of space, a new hash table is created with double the amount of slots and rehash all of the values again.
When the load factor is greater than 0.7, it's time to resize the hash table.

A great way to avoid collisions is to keep the load factor low and have a good hash function. A good hash function 
distributes values in the array well whereas a bad one creates lots of collisions.

#### Runtime complexities:
Hash Tables:
Average case:
* Search: O(1)
* Insert: O(1)
* Delete: O(1)

Worst case:
* Search: O(n)
* Insert: O(n)
* Delete: O(n)

Linear time (simple search) has a runtime of O(n).
Binary search is faster with a runtime of O(log n).
Hash tables have a constant runtime of O(1).

The size of the hash table doesn't matter, it won't affect the runtime.


#### Exercise:
5.1: Consistent

5.2: Not consistent

5.3: Not consistent

5.4: The book says consistent but I believe it's not consistent since even though a string is immutable, 
you can always append to it by resetting the variable or change it.

5.5: D is a good distribution. The book says C would be good too but I already see a collision so I disagree.

5.6: B and D are good distributions.

5.7: C and D are good distributions. The book says B would be good too but I already see a collision so I disagree.