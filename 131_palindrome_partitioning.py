class Solution:
	def partition(self, s: str) -> list[list[str]]:
		res = []
		path = []
		
		# 判断回文
		def is_pal(sub):
			left = 0
			right = len(sub) - 1
			while left < right:
				if sub[left] != sub[right]:
					return False
				if sub[left] == sub[right]:
					left += 1
					right -= 1
			return True
		
		def dfs(start):
			# 切到末尾，收集一个完整分割方案
			if start == len(s):
				res.append(path[:])
				return
			
			for i in range(start, len(s)):
				sub = s[start:i + 1]  # 当前这一刀切出的段
				if not is_pal(sub):  # 不是回文，换更长的一段再试
					continue
				path.append(sub)  # 放
				dfs(i + 1)  # 下一段从 i+1 开始
				path.pop()  # 撤销
		
		dfs(0)
		return res


