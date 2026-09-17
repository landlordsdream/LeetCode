class ListNode:
	def __init__(self, key: int, val: int):
		self.key = key
		self.val = val
		self.prev = None
		self.next = None


class LRUCache:
	
	def __init__(self, capacity: int):
		# 这里应该是用双向链表和哈希表
		# 创建双向链表 和 哈希表
		# head tail 两个哨兵 非循环链表
		self.capacity = capacity
		self.cache = {}
		self.head = ListNode(-1, -1)
		self.tail = ListNode(-1, -1)
		self.head.next = self.tail
		self.tail.prev = self.head
	
	def _remove_tail(self):
		
		node = self.tail.prev
		node.prev.next = self.tail
		self.tail.prev = node.prev
		return node
	
	def _add_to_head(self, node: ListNode):
		node.prev = self.head
		node.next = self.head.next
		self.head.next.prev = node
		self.head.next = node
	
	def _remove_to_head(self, node: ListNode):
		node.prev.next = node.next
		node.next.prev = node.prev
		self._add_to_head(node)
	
	def get(self, key: int) -> int:
		if key not in self.cache:
			return -1
		curr = self.cache[key]
		self._remove_to_head(curr)
		return self.cache[key].val
	
	def put(self, key: int, value: int) -> None:
		if key in self.cache:
			node = self.cache[key]
			node.val = value
			self._remove_to_head(node)
		else:
			curr = ListNode(key, value)
			self.cache[key] = curr
			self._add_to_head(curr)
			if len(self.cache) > self.capacity:
				removed = self._remove_tail()
				del self.cache[removed.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)