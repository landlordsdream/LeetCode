class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if not grid:
			return 0
		# 行与列
		rows, cols = len(grid), len(grid[0])
		# 计数
		count = 0
		
		# dfs 用于标记已访问
		def dfs(i, j):
			# 越界或者不是陆地 返回
			if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
				return
			# 标记当前已访问
			grid[i][j] = '0'
			dfs(i + 1, j)
			dfs(i - 1, j)
			dfs(i, j + 1)
			dfs(i, j - 1)
		
		for i in range(rows):
			for j in range(cols):
				if grid[i][j] == '1':
					count += 1
					dfs(i, j)
		return count

