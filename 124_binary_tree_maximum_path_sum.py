# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxPathSum(self, root: TreeNode | None) -> int:
		self.result = float('-inf')
		
		# 第一感觉是和为targetsum 那题的思路加上 也就是前缀和 加上不断比较取max
		# 好吧思路错了 是上一题124题思路深度优先
		def maxsum(node):
			if not node:
				return 0
			# 只有在贡献值大于0时 才会选取子节点
			left = max(maxsum(node.left), 0)
			right = max(maxsum(node.right), 0)
			
			self.result = max(left + right + node.val, self.result)
			
			return node.val + max(left, right)
		
		maxsum(root)
		return self.result

