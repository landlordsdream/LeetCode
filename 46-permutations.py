class Solution:
	def permute(self, nums: list[int]) -> list[list[int]]:
		# DFS回溯
		# 首先是没思路的 先定义结果
		res = []
		# 想象盒子放球 标记使用过的球 和nums对应 nums[i] used[i]
		used = [False] * len(nums)
		# 补一个标量 当前盒子里放了那些球 记录答案
		path = []
		
		def dfs():
			# 结束条件 当盒子里的球数量等于len(nums)
			if len(path) == len(nums):
				# res.append(path) 这里是path对象本身的引用 存引用 最后会变成[]
				
				# 这里引入拷贝path[:]
				res.append(path[:])
				# 本来我想该回溯处理上一层 的球了 提示该返回上一层 让上一层去选择
				return
			# 想象填第k个盒子 看剩下的球那个能用 即遍历所有 关键思维 逐个尝试 跳过used
			for i in range(len(nums)):
				if used[i]:
					continue
				# 放球
				used[i] = True
				path.append(nums[i])
				# 下一层 递归
				dfs()
				# 然后拿回来 遍历下一个
				# used[i] = False
				# path.pop()
				# 好习惯 对称
				path.pop()
				used[i] = False
		
		# 启动与返回
		dfs()
		return res





