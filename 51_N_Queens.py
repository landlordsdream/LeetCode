class Solution:
	def solveNQueens(self, n: int) -> list[list[str]]:
		res = []
		# 臭棋篓子
		
		board = [['.'] * n for _ in range(n)]
		# 每行的皇后攻击同列 主对角线 副对角线
		col = set()
		diag1 = set()
		diag2 = set()
		
		def dfs(row):
			if row == n:
				res.append(["".join(r) for r in board])
				return
			for c in range(n):
				if c in col or row - c in diag1 or row + c in diag2:
					continue
				board[row][c] = 'Q'
				col.add(c)
				diag1.add(row - c)
				diag2.add(row + c)
				dfs(row + 1)
				diag2.remove(row + c)
				diag1.remove(row - c)
				col.remove(c)
				board[row][c] = '.'
		
		dfs(0)
		return res


