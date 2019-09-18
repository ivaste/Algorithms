#General tree
#............................

# Definition for a Node.
class Node(object):
	def __init__(self, val, children):
		self.val = val
		self.children = children


def preorder(self, root):	#O(n)
	l=[]
	if root is not None:
		l.append(root.val)
		for n in root.children:
			l+=self.preorder(n)
	return l
	
	
def postorder(self, root):
	l=[]
	if root is not None:
		for n in root.children:
		l=l+self.postorder(n)
		l.append(root.val)
	return l
	
def levelOrder(self, root):
	if root is None:
		return []
	
	output=[]
	Q=[root,] #Queue FIFO
	while Q:
		l=[]
		q2=[]
		for n in Q:
			l.append(n.val)
			q2+=n.children
		Q=q2
		output.append(l)
	return output