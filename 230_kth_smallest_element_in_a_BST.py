# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		self.val = float('-inf')
		self.count = 0
		
		def inorder(node):
			if not node or self.count == k:
				return
			inorder(node.left)
			self.count += 1
			if self.count == k:
				self.val = node.val
				return
			
			inorder(node.right)
		
		inorder(root)
		return self.val
