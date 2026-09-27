# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def flatten(self, root: TreeNode | None) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		self.prev = None
		
		def prevorder(node):
			if not node:
				return
			left = node.left
			right = node.right
			
			# 处理当前节点 接到self.prev.right 存在直接接后面 头结点时 prev == None 和后面一个逻辑 直接 指向下一个节点 即头结点 所以不用else
			if self.prev:
				self.prev.right = node
			node.left = None
			self.prev = node
			prevorder(left)
			prevorder(right)
		
		prevorder(root)

