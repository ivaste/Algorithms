#Binary tree
#...............................

class Node(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
		
		
def preorderTraversal(self, root):
	if root is None:
		return []
	l=[root.val,]
	l+=self.preorderTraversal(root.left)
	l+=self.preorderTraversal(root.right)
	return l
	
def inorderTraversal(self, root):
	if root is None:
		return []
	output=[]
	output+=self.inorderTraversal(root.left)
	output.append(root.val)
	output+=self.inorderTraversal(root.right)
	return output
	
	
def postorderTraversal(self, root):
	if root is None:
		return []
	l=[]
	l+=self.postorderTraversal(root.left)
	l+=self.postorderTraversal(root.right)
	l.append(root.val)
	return l
	
	
def levelOrder(self, root):
	if root is None:
		return []
		
	output=[]
	queue=[root,]

	while queue:
		l=[]
		Q2=[]
		for n in queue:
			l.append(n.val)
			if n.left is not None:
				Q2.append(n.left)
			if n.right is not None:
				Q2.append(n.right)
		queue=Q2
		output.append(l)

	return output