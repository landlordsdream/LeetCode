# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		# 第一反应深度优先搜索 然后找到pq 再用递归回溯得到结果
		self.result_node = None
		
		def dfs(node):
			if not node:
				return 0
			left_count = dfs(node.left)
			right_count = dfs(node.right)
			self_count = 0
			if node == q or node == p:
				self_count = 1
			total = left_count + right_count + self_count
			if total == 2 and self.result_node is None:
				self.result_node = node
			
			return total
		
		total = dfs(root)
		
		return self.result_node

