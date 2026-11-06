class Solution:
	def letterCombinations(self, digits: str) -> list[str]:
		# 肯定有拆分字符串这一步骤然后遍历每个字符 像子集一样返回对应的字符串
		res = []
		# 边界
		if not digits:
			return []
		mapping = {
			"2": "abc",
			"3": "def",
			"4": "ghi",
			"5": "jkl",
			"6": "mno",
			"7": "pqrs",
			"8": "tuv",
			"9": "wxyz",
		}
		path = []
		
		def dfs(index):
			if index == len(digits):
				# 看题意 列表转字符串
				# "".join(path)   本身产生新字符串"ab" 所以不用拷贝
				res.append("".join(path))
				return
			letter = mapping[digits[index]]
			for ch in letter:
				path.append(ch)
				dfs(index + 1)
				path.pop()
		
		dfs(0)
		return res
