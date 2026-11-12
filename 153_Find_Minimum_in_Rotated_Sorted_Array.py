class Solution:
	def findMin(self, nums: list[int]) -> int:
		l, r = 0, len(nums) - 1
		
		while l < r:
			mid = (l + r) // 2
			if nums[mid] > nums[r]:
				# 左半段有序 最小值在右边
				l = mid + 1
			else:
				# 右半段有序 最小值在mid or mid左边
				r = mid
		
		return nums[l]

