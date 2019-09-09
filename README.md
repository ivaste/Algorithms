# Data Structures and Algorithms
Quick reference of Data Structures and Algorithms in Python to easily pass coding interviews.

....WORK IN PROGRESS....

## Data Structures
 - [Big O]()
 - [Array and Strings]()
 - [Hash Tables](#Hash Tables)
 - [Stacks](#Stacks)
 - [Queues]()
 - [Trees]()
 - [Tries]()
 - [Graphs]()
 - [Heaps]()

## Algorithms
 - [...]()


<details>
<summary>Big O</summary>
<img src="https://github.com/ivaste/Algorithms/blob/master/BigO_Algorithms.JPG"/>
<img src="https://github.com/ivaste/Algorithms/blob/master/BigO_Sort.JPG" max/>

</details>


<details><summary>Hash Tables</summary>
....
blablabla
</details>

##Stacks

*Last-in, first-out (LIFO)* principle. 
Used to:
- reverse a data sequence.
- Recursive algorithms to store data and pick them up lately
- To implement a recursive algorithm iteratively

Methods:
- *S.push(e):* Add element e to the top of stack S.
- *S.pop():* Remove and return the top element from the stack S; an error occurs if the stack is empty.
-	*S.top():* Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
-	*S.is_empty( ):* Return True if stack S does not contain any elements.
-	*len(S):* Return the number of elements in stack S; __len__
A newly created stack is empty.

*Implementation* with a Single Linked List: [LinkedStack.py](https://github.com/ivaste/Algorithms/blob/master/LinkedStack.py)

*Time Complexity:*
| Operation   | Running Time |
| ----------- |-------------:|
| S.push()    | O(1)         |
| S.pop()     | O(1)         |
| S.top()     | O(1)         |
| len(S)      | O(1)         |
| S.isEmpty() | O(1)         |

*Space Complexity:* O(n)

