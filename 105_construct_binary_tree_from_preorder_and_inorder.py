# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
		# 四指针 哈希表 以空间换时间
		# 以val为键 获取该值在中序遍历下标位置
		index_map = {val: i for i, val in enumerate(inorder)}
		
		def build(pre_left, pre_right, in_left, in_right):
			# 如果在先序遍历序列中区间为空 表示已没有子树需要构建
			if pre_left > pre_right:
				return None
			# 先序区间第一个为子树根节点
			root_val = preorder[pre_left]
			root = TreeNode(root_val)
			
			mid = index_map[root_val]
			left_size = mid - in_left
			
			root.left = build(pre_left + 1, pre_left + left_size, in_left, mid - 1)
			root.right = build(pre_left + left_size + 1, pre_right, mid + 1, in_right)
			
			return root
		
		return build(0, len(preorder) - 1, 0, len(inorder) - 1)








