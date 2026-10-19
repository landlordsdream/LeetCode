# 基础数据结构 字典 键值对 key 字符"a" valve 字符'b' 的TrieNode对象
# 节点B.children = {
#     'p': 节点C,  # 连向 'p'，准备拼 'app'
#     'e': 节点D   # 连向 'e'，准备拼 'ape'
# }
class TrieNode:
	def __init__(self):
		self.children = {}
		self.is_end = False


class Trie:
	
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, word: str) -> None:
		node = self.root
		for character in word:
			if character not in node.children:
				node.children[character] = TrieNode()
			node = node.children[character]
		node.is_end = True
	
	def search(self, word: str) -> bool:
		node = self.root
		for character in word:
			if character not in node.children:
				return False
			node = node.children[character]
		return node.is_end
	
	def startsWith(self, prefix: str) -> bool:
		node = self.root
		for character in prefix:
			if character not in node.children:
				return False
			node = node.children[character]
		return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)