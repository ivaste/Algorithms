''' 
  HEAD                                       TAIL
 ________      ________      ________      ________ 
|      | |    |      | |    |      | |    |      | |
| None | |--->|  a   | |--->|  b   | |--->|  c   | |--->None
|______|_|    |______|_|    |______|_|    |______|_|

Main Methods: isEmpty, addFirst, addLast, removeFirst, removeLast, makeEmpty
'''
# Exception when attempting to access an element from an empty container.
class EmptyLinkedList(Exception):
	pass
	
class SingleLinkedList:
	
  #-------------------------- nested _Node class --------------------------
  class _Node:
    __slots__ = '_element', '_next'            			# streamline memory for faster attribute access, and space savings in memory.

    def __init__(self, element=None, next=None):    # initialize node's fields
      self._element = element                  			# user's element
      self._next = next                        			# next node reference


  #-------------------------- list constructor --------------------------
  def __init__(self):
    #Create empty LinkedList
    self._head = self._tail = self._Node()
    self._size = 0
	
	#-------------------------- public accessors --------------------------
  def __len__(self):
    return self._size								#Return the number of elements in the list.

  def isEmpty(self):
    return self._head==self._tail		#Return True if list is empty.
		
	def addFirst(self, element):			#O(1)
    self._head._element=element
    n=self._Node(None,self._head)
    self._head=n
		self._size+=1
		
	def addLast(self, element):				#O(1)
    n=self._Node(element, None)
    self._tail._next=n
    self._tail=n
		self._size+=1
		
	def removeFirst(self):		#O(1)
		if isEmpty():
			raise EmptyLinkedList()
		e=self._head._next._element
		self._head=self._head._next
		self._head._element=None
		self._size-=1
		return e
		
	def removeLast(self):			#O(n)
		e=self._tail._element
		temp=self._head
		while(temp!=self._tail):
			temp=temp._next
		self._tail=temp
		self._tail._next=None
		self._size-=1
		return e
		
	def makeEmpty(self):
		self._head = self._tail = Node()	#None node
		self._size = 0
