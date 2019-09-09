# Exception when attempting to access an element from an empty container.
class Empty(Exception):
	pass

# LIFO Stack implementation using a singly linked list for storage
class LinkedStack:

  #-------------------------- nested _Node class --------------------------
  class _Node:
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):      # initialize node's fields
      self._element = element               # reference to user's element
      self._next = next                     # reference to next node

  #------------------------------- stack methods -------------------------------
  def __init__(self):
    self._head = None                       # reference to the head node
    self._size = 0                          # number of stack elements

  def __len__(self):
    return self._size

  def is_empty(self):
    return self._size == 0

  def push(self, e):
    self._head = self._Node(e, self._head)  # create and link a new node
    self._size += 1

  def top(self):
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._head._element              # top of stack is at head of list

  def pop(self):
    if self.is_empty():
      raise Empty('Stack is empty')
    answer = self._head._element
    self._head = self._head._next           # bypass the former top node
    self._size -= 1
    return answer
