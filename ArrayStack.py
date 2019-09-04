# Exception when attempting to access an element from an empty container.
class Empty(Exception):
	pass
	
#LIFO Stack implementation using a Python list as underlying storage.
class ArrayStack:

	def __init__(self):
		#Create an empty stack.
		self._data = [] 		# nonpublic list instance
	
	def __len__(self):	#O(1)
		#Return the number of elements in the stack.
		return len(self._data)
	
	def is_empty(self):	#O(1)
		#Return True if the stack is empty.
		return len(self._data) == 0
	
	def push(self, e):	#O(1) amortized
		#Add element e to the top of the stack.
		self._data.append(e) # new item stored at end of list
	
	def top(self):	#O(1)
		#Return (but do not remove) the element at the top of the stack.
		#Raise Empty exception if the stack is empty.
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data[-1] # the last item in the list
	
	def pop(self):	#O(1) amortized
		#Remove and return the element from the top of the stack (i.e., LIFO).
		#Raise Empty exception if the stack is empty.
		if self.is_empty( ):
			raise Empty("Stack is empty")
		return self._data.pop() 		# remove last item from list