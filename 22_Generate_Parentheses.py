class Solution:
	def generateParenthesis(self, n: int) -> list[str]:
		res = []
		
		# 已放左括号和右括号数 left right
		path = []
		
		def dfs(left, right):
			if left == n and right == n:
				res.append("".join(path))
				return
			if left < n:
				path.append("(")
				dfs(left + 1, right)
				path.pop()
			if right < left:
				path.append(")")
				dfs(left, right + 1)
				path.pop()
