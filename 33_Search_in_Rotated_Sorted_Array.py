class Solution:
	def search(self, nums: list[int], target: int) -> int:
		l, r = 0, len(nums) - 1
		while l <= r:
			mid = (l + r) // 2
			if nums[mid] == target:
				return mid
			# 局部二分
			if nums[l] <= nums[mid]:
				# 左边有序
				if nums[l] <= target < nums[mid]:
					# 目标在左半边
					r = mid - 1
				else:
					l = mid + 1
			else:
				if nums[mid] < target <= nums[r]:
					# 目标在右半边
					l = mid + 1
				else:
					r = mid - 1
		return -1
