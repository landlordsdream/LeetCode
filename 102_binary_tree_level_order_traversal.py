# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
	def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
		if not root:
			return []
		queue = deque([root])
		result = []
		while queue:
			
			level_size = len(queue)
			level_node_val = []
			for _ in range(level_size):
				node = queue.popleft()
				level_node_val.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			result.append(level_node_val)
		return result
