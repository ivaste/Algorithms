#Trie. Each node has a map {} that stores its children.
# If the node represent the end of a word, a special character "#" in the map is used as a FLAG
class Trie:

	def __init__(self):
		self.root = {}
			

	def insert(self, word: str) -> None:
		trie = self.root
		
		for i in word:
			# add letter if not present as a child
			if i not in trie:
				trie[i] = {}
			
			# enter childe node
			trie = trie[i]
		
		#attach end-of-word indicator
		trie["#"] = "#"
			
	def search(self, word: str) -> bool:
		trie = self.root
		
		for i in word:
			if i not in trie:
				return False
			trie = trie[i]
		
		if "#" in trie:
			return True
		
		return False


	def startsWith(self, prefix: str) -> bool:
		trie = self.root
		
		for i in prefix:
			if i not in trie:
				return False
			
			trie = trie[i]
		
		return True