class Solution:
	def subsets(self, nums: list[int]) -> list[list[int]]:
		# 首先是结果res
		res = []
		
		# 然后是路径path
		path = []
		
		def dfs(start):
			# 不需要讲顺序 空集也包含 则起始位置每一层往后选
			# 收集结果
			res.append(path[:])
			for i in range(start, len(nums)):
				# 放球
				path.append(nums[i])
				dfs(i + 1)
				path.pop()
		
		dfs(0)
		return res


