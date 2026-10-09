class Solution:
	def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
		# 首先 建图 邻接表
		#         graph = [
		#     [1],    # 0 → 1
		#     [2],    # 1 → 2
		#     [3],    # 2 → 3
		#     []      # 3 没有后继
		# ]
		graph = [[] for _ in range(numCourses)]
		for a, b in prerequisites:
			graph[b].append(a)
		
		# 三色标记 0 1 2 未访问 访问中 已完成 一个节点所有邻居都处理完 且没有发现环
		state = [0] * numCourses
		
		def dfs(node):
			# 如果该节点在访问中 则出现环
			if state[node] == 1:
				return False
			# 如果该节点所有邻居处理完 且没有发现环
			if state[node] == 2:
				return True
			# 标记当前节点为访问中
			state[node] = 1
			# 处理当前节点所有邻居节点
			for neighbor in graph[node]:
				if not dfs(neighbor):
					return False
			# 处理完当前节点所有邻居节点后
			state[node] = 2
			return True
		
		for i in range(numCourses):
			if not dfs(i):
				return False
		return True


