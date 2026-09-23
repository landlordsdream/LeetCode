# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isValidBST(self, root: TreeNode | None) -> bool:
		# 推荐中序遍历
		# self.prev node前一个节点值
		# 结果返回 self.valid 初始为True
		self.prev = float('-inf')
		self.valid = True
		
		def inorder(node):
			if not node or not self.valid:
				return
			inorder(node.left)
			if self.prev < node.val:
				self.prev = node.val
			else:
				self.valid = False
				return
			inorder(node.right)
		
		inorder(root)
		
		return self.valid

