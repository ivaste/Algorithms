# Data Structures and Algorithms
Quick reference of Data Structures and Algorithms in Python to easily pass coding interviews.

# ....WORK IN PROGRESS....

### Data Structures
 - [Big O](#Big)
 - [Array and Strings](#Array)
 - [Hash Tables](#Hash)
 - [Stacks](#Stacks)
 - [Queues](#Queues)
 - [Trees](#Trees)
 - [Tries](#Tries)
 - [Graphs](#Graphs)
 - [Heaps](#Heaps)

### Algorithms
 - [...]()


## Big O
<details>
<img src="https://github.com/ivaste/Algorithms/blob/master/BigO_Algorithms.JPG"/>
<img src="https://github.com/ivaste/Algorithms/blob/master/BigO_Sort.JPG" max/>

</details>


## Hash Tables
....
blablabla


## Stacks

**Last-in, first-out (LIFO)** principle. 
Used to:
- Reverse a data sequence.
- Recursive algorithms to store data and pick them up lately
- To implement a recursive algorithm iteratively

**Methods:**
- **S.push(e):** Add element e to the top of stack S.
- **S.pop():** Remove and return the top element from the stack S; an error occurs if the stack is empty.
-	**S.top():** Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
-	**S.is_empty( ):** Return True if stack S does not contain any elements.
-	**len(S):** Return the number of elements in stack S; \_\_len\_\_

A newly created stack is empty.

**Implementation** with a Single Linked List: [LinkedStack.py](https://github.com/ivaste/Algorithms/blob/master/LinkedStack.py)

**Time Complexity:**

| Operation   | Running Time |
| ----------- |-------------:|
| S.push()    | O(1)         |
| S.pop()     | O(1)         |
| S.top()     | O(1)         |
| len(S)      | O(1)         |
| S.isEmpty() | O(1)         |

**Space Complexity:** O(n)


## Queues

**First-in, first-out (FIFO)** principle.

Used in:
-	breadth first search
-	implementing a cache

**Methods:**
-	**Q.enqueue(e):** Add element e to the back of queue Q.
-	**Q.dequeue():** Remove and return the first element from queue Q; an error occurs if the queue is empty.
-	**Q.first():** Return a reference to the element at the front of queue Q, without removing it; an error occurs if the queue is empty.
-	**Q.isEmpty():** Return True if queue Q does not contain any elements.
-	**len(Q):** Return the number of elements in queue Q; \_\_len\_\_

A newly created queue is empty.

**Implementation** with a Single Linked List: [LinkedQueue.py](https://github.com/ivaste/Algorithms/blob/master/LinkedQueue.py)

**Time Complexity:**

| Operation    | Running Time |
| -----------  |-------------:|
| Q.enqueue(e) | O(1)         |
| Q.dequeue()  | O(1)         |
| Q.first()    | O(1)         |
| Q.isEmpty()  | O(1)         |
| len(Q)       | O(1)         |

**Space Complexity:** O(n)