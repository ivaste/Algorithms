#Binary Search tree
#...............................

class Node(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		

#Time: O(h)=O(logn), Space: O(h)=O(logn)
def searchBST(self, root, val):
	if root is None:
		return None
	if root.val == val:
		return root
	elif val<root.val:
		return self.searchBST(root.left,val)
	else:
		return self.searchBST(root.right,val)



def search(self, root, val):
	if root.val==val:
		return root
	elif root.left and val<root.val:
		return self.search(root.left,val)
	elif root.right and val>root.val:
		return self.search(root.right,val)
	return None #or return root when using insertion.  Unsuccessful search
	
def insertion(self, root, val):
	n=self.search(root, val)
	if val==n.val:
		return
	elif val<n.val:
		n.left=TreeNode(val)
	else:
		n.right=TreeNode(val)
	return root
	
	
def successor(self, root):
	"""
	One step right and then always left
	"""
	root = root.right
	while root.left:
		root = root.left
	return root.val

def predecessor(self, root):
	"""
	One step left and then always right
	"""
	root = root.left
	while root.right:
		root = root.right
	return root.val
		
def deleteNode(self, root, key):
	if not root:
		return None
	
	# delete from the right subtree
	if key > root.val:
		root.right = self.deleteNode(root.right, key)
	# delete from the left subtree
	elif key < root.val:
		root.left = self.deleteNode(root.left, key)
	# delete the current node
	else:
		# the node is a leaf
		if not (root.left or root.right):
			root = None
		# the node is not a leaf and has a right child
		elif root.right:
			root.val = self.successor(root)
			#Remove the successor
			root.right = self.deleteNode(root.right, root.val)
		# the node is not a leaf, has no right child, and has a left child    
		else:
			root.val = self.predecessor(root)
			#Remove the predecessor
			root.left = self.deleteNode(root.left, root.val)
								
	return root