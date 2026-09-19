# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isSymmetric(self, root: TreeNode | None) -> bool:
		if not root:
			return True
		
		def isMirror(left, right):
			if left is None and right is None:
				return True
			elif left is None or right is None:
				return False
			if left.val != right.val:
				return False
			B1 = isMirror(left.left, right.right)
			B2 = isMirror(left.right, right.left)
			return B1 and B2
		
		return isMirror(root.left, root.right)
