class Solution:
	def exist(self, board: list[list[str]], word: str) -> bool:
		m = len(board)
		n = len(board[0])
		visited = [[False] * n for _ in range(m)]
		target = len(word)
		# 定义方向向量
		dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		
		def dfs(i, j, k):
			if i < 0 or i >= m or j < 0 or j >= n:
				return False
			if visited[i][j]:
				return False
			if board[i][j] != word[k]:
				return False
			if k == target - 1:
				return True
			visited[i][j] = True  # 标记当前路径上已经用过了
			for di, dj in dirs:
				if dfs(di + i, dj + j, k + 1):
					visited[i][j] = False
					return True
			visited[i][j] = False  # 四个方向都试过了 让其他路径可以用这个格子
			return False
		
		for i in range(m):
			for j in range(n):
				if dfs(i, j, 0):
					return True
		return False

