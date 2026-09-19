# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0
		diameter = 0
		self.max_length = 0
		
		def length(node):
			if not node:
				return 0
			left = length(node.left)
			right = length(node.right)
			self.max_length = max(self.max_length, left + right)
			return max(left, right) + 1  # 边数
		
		length(root)
		return self.max_length
