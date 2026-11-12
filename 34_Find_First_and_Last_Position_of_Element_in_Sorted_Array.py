class Solution:
	def searchRange(self, nums: list[int], target: int) -> list[int]:
		def lower_bound(t: int) -> int:
			# 第一个大于等于target(待插入位置)
			left, right = 0, len(nums)  # 左闭右开[0,n)
			while left < right:
				mid = (left + right) // 2
				if nums[mid] < t:
					left = mid + 1
				else:
					right = mid
			return left
		
		start = lower_bound(target)
		if start == len(nums) or nums[start] != target:
			return [-1, -1]
		end = lower_bound(target + 1) - 1
		return [start, end]


