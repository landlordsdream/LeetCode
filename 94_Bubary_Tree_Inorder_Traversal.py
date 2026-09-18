# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def inorderTraversal(self, root: TreeNode | None) -> list[int]:
		result = []
		def inorder(node):
			if not node:
				return
			inorder(node.left)
			result.append(node.val)
			inorder(node.right)
		inorder(root)
		return result
		
		
class Solution:
	def inorderTraversal(self, root: TreeNode | None) -> list[int]:
		if not root:
			return []
		result = []
		stack = []
		curr = root
		while curr or stack:
			# 动作A 一直向左压栈
			while curr:
				stack.append(curr)
				curr = curr.left
			# 弹栈访问 转向右
			curr = stack.pop()
			result.append(curr.val)
			curr = curr.right
		return result
		