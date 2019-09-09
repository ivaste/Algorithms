'''      IMPLEMENTATION METHOD 2 (less common but easier)
  HEAD                                      TAIL
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
		return self._size==0		#Return True if list is empty.

	def addFirst(self, element):			#O(1)
		self._head._element=element
		self._head=self._Node(None,self._head)
		self._size+=1

	def addLast(self, element):				#O(1)
		self._tail._next=self._Node(element,None)
		self._tail=self._tail._next
		self._size+=1

	def removeFirst(self):		#O(1)
		if self.isEmpty():
			raise EmptyLinkedList()
		e=self._head._next._element
		self._head=self._head._next
		self._head._element=None
		self._size-=1
		return e
	
	def removeLast(self):			#O(n)
		if self.isEmpty():
			raise EmptyLinkedList()
	
		e=self._tail._element
		n=self._head
		while n._next!=self._tail:
			n=n._next
		
		self._tail=n
		self._tail._next=None
		self._size-=1
		return e

	def makeEmpty(self):
		self._head = self._tail = self._Node()
		self._size = 0

	def getContent(self):
		l=[]
		n=self._head
		while n._next!= None:
			n=n._next
			l.append(n._element)
		return l
