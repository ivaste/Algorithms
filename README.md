# Data Structures and Algorithms
Quick reference of Data Structures and Algorithms in Python to easily pass coding interviews.

# ....WORK IN PROGRESS....

### Data Structures
 - [Big O](#Big-O)
 - [Array and Strings](#Array-and-Strings)
 - [Hash Tables](#Hash-Tables)
 - [Linked List](#Linked-List)
 - [Stacks](#Stacks)
 - [Queues](#Queues)
 - [Trees](#Trees)
  - [General Trees](#General-Trees)
	- [Binary Trees](#Binary-Trees)
	- [Traversal Algorithms](#Traversal-Algorithms)
	- [Solve Tree problems recursively](#Solve-Tree-problems-recursively)
 - [Search Trees](#Search-Trees)
  - [Binary Search Trees](#Binary-Search-Trees)
	- [Balanced Search Trees](#Balanced-Search-Trees)
	- [AVL Trees](#AVL-Trees)
	- [Red-Black Trees](#Red-Black-Trees)
 - [Tries](#Tries)
 - [Graphs](#Graphs)
 - [Heaps](#Heaps)

### Algorithms
 - [...]()


## Big O
<details>
<img src="https://github.com/ivaste/Algorithms/blob/master/BigO_Algorithms.JPG"/>
<img src="https://github.com/ivaste/Algorithms/blob/master/BigO_Sort.JPG"/>

</details>


## Array and Strings
......

<!-- ------------------------------------------------------------------- -->

## Hash Tables
....


<!-- ------------------------------------------------------------------- -->

## Linked List
Advantages of Array-Based Sequences
-	O(1)-time access to an element based on an integer index. in a linked list requires O(k)
-	O(1) operations typically are more efficient.
-	typically use proportionally less memory than linked structures.
Advantages of Link-Based Sequences:
-	provide worst-case time bounds for their operations. In contrast to the amortized bounds associated with the expansion or contraction of a dynamic array.
-	O(1)-time insertions and deletions at arbitrary positions with the PositionalList class

Solution techniques:
-	In an interview, you must understand whether it is a singly linked list or a doubly linked list.
-	**The "Runner" Technique:** iterate through the linked list with two pointers simultaneously, with one ahead of the other. The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each one node that the "slow" node iterates through.
-	Many LinkedList problems involve **recursion**.

**Time Complexity:**

| Operation       | Running Time |
| --------------- |-------------:|
| L.addFirst(e)   | O(1)         |
| L.addLast(e)    | O(1)         |
| L.removeFirst() | O(1)         |
| L.removeLast()  | **O(n)**     |
| L.isEmpty()     | O(1)         |
| len(L)          | O(1)         |

### Singly Linked Lists
Each node stores a reference to an object and a reference to the next node of the list.
First and last node are known as the **head** and **tail**
<p align="center">
<img src="https://github.com/ivaste/Algorithms/blob/master/Images/SinglyLinkedList.JPG"/>
</p>
The linked list instance must keep a reference to the head of the list. Often is also stored a reference to the tail.

**Implementations:**
- [SingleLinkedList.py](https://github.com/ivaste/Algorithms/blob/master/SingleLinkedList.py) (More common)
- [SingleLinkedList2.py](https://github.com/ivaste/Algorithms/blob/master/SingleLinkedList2.py) (Less common but easier)

### Doubly Linked Lists
Each node keeps an explicit reference to the node before it and a reference to the node after it.
Allow a greater variety of O(1)-time update operations, including insertions and deletions at arbitrary positions within the list.

Special nodes at both ends of the list: a header node at the beginning of the list, and a trailer node at the end of the list. They do not store elements.
<p align="center">
<img src="https://github.com/ivaste/Algorithms/blob/master/Images/DoublyLinkedList.JPG"/>
</p>
An empty list is initialized so that the next field of the header points to the trailer, and the prev field of the trailer points to the header.

**Implementation:** [DoublyLinkedBase.py](https://github.com/ivaste/Algorithms/blob/master/DoublyLinkedBase.py)

### Positional Linked Lists
Provides a user a way to refer to elements anywhere in a sequence, and to perform arbitrary insertions and deletions.

continue.....

<!-- ------------------------------------------------------------------- -->

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
| S.push(e)   | O(1)         |
| S.pop()     | O(1)         |
| S.top()     | O(1)         |
| S.isEmpty() | O(1)         |
| len(S)      | O(1)         |

**Space Complexity:** O(n)


<!-- ------------------------------------------------------------------- -->

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


<!-- ------------------------------------------------------------------- -->

## Trees

Node class:
''
class Node(object):
	def __init__(self, val, children):
		self.val = val
		self.children = children
''

Tree class: in interviews typically is not used.

### General Trees
**Tree** _T_ is a set of **nodes** storing elements such that the nodes have a parent-child relationship that satisfies the following properties:
 - If _T_ is nonempty, it has a special node, called the **root** of _T_, that has no parent.
 - Each node _v_ of _T_ different from the root has a unique **parent** node _w_; every node with parent _w_ is a **child** of _w_.


**Edge:** pair of nodes (u,v) such that u is the parent of v, or vice versa
**Path:** sequence of nodes such that any two consecutive nodes in the sequence form an edge.
**Ancestor:** x is ancestor of y if x=y or x is ancestor of the father of y
**Descendant:** x is descendant of y if y is ancestor of x
**Internal nodes:** nodes with at least 1 child
**External nodes (leaf):** nodes without children


**Ordered Tree:** if there is a meaningful linear order among the children of each node; arranging siblings left to right, according to their order.

**Depth** of a node (2 ways):
 - <img src="https://latex.codecogs.com/gif.latex?depth_T(v)=abs(ancestors(v))-1" />
 - ...

...
### Binary Trees
...
### Traversal Algorithms
...
### Solve Tree problems recursively
...


<!-- ------------------------------------------------------------------- -->

## Search Trees
....

### Binary Search Trees
...
### Balanced Search Trees
...
### AVL Trees
...
### Red-Black Trees
...
