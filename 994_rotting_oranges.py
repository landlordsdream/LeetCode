from collections import deque


class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:
		rows, cols = len(grid), len(grid[0])
		queue = deque()
		flesh = 0
		# 收集所有烂橘子作为第一层
		for i in range(rows):
			for j in range(cols):
				if grid[i][j] == 2:
					queue.append((i, j))
				elif grid[i][j] == 1:
					flesh += 1
		
		# 如果没有新鲜橘子
		if flesh == 0:
			return 0
		
		minutes = 0
		
		# 循环遍历
		while queue:
			level_size = len(queue)
			for _ in range(level_size):
				i, j = queue.popleft()
				for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
					ni, nj = i + di, j + dj
					# 越界不访问 所以判断条件直接先检查邻居合法才进入
					if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
						grid[ni][nj] = 2
						queue.append((ni, nj))
						flesh -= 1
			if queue:
				minutes += 1
		# 没有新鲜橘子 或者 该橘子永远不会腐烂
		return minutes if flesh == 0 else -1

