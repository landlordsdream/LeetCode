# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
		# 构建函数从某个节点出发， 向下计算
		
		def count_from(node, target):
			if not node:
				return 0
			count = 1 if node.val == target else 0
			count += count_from(node.left, target - node.val)
			count += count_from(node.right, target - node.val)
			return count
		
		# 遍历整个root
		if not root:
			return 0
		return count_from(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

# 进阶：哈希表 + 前缀和 + 回溯，O(n)
# prefix_sum = {0: 1}  ← 关键：0 表示"空路径"，让从根出发的路径也能被统计
# 进入节点：先查 curr_sum - targetSum，再把 curr_sum 存入哈希表
# 离开节点：回溯，prefix_sum[curr_sum] -= 1，保证只统计当前路径
# 这样哈希表里永远只有"从根到当前节点"这条路径上的前缀和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
		# 前缀和与深度优先搜索DFS 结合
		# 前缀和哈希表
		prefix_sum = {0: 1}
		
		def DFS(node, curr_sum):
			# 接受节点与当前前缀和
			if not node:
				return 0
			# 更新当前前缀和
			curr_sum += node.val
			# 因为要找的是祖先的前缀和 所以 查询 如果在字典里则返回 不存在时返回0
			count = prefix_sum.get(curr_sum - targetSum, 0)
			# 将当前前缀和加入到 prefix_sum
			prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
			count += DFS(node.left, curr_sum)
			count += DFS(node.right, curr_sum)
			return count
		
		return DFS(root, 0)
		
		return DFS(root, 0)



