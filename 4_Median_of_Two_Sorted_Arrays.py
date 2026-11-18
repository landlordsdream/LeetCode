class Solution:
	def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1
		m, n = len(nums1), len(nums2)
		# 左半部分最大 或者 左半部分最大+ 右半部分最小 // 2
		total_left = (m + n + 1) // 2
		left, right = 0, m
		# i = (left + right) // 2
		# j = total_left - i
		
		while left <= right:
			i = (left + right) // 2
			j = total_left - i
			nums1_left = nums1[i - 1] if i > 0 else float('-inf')
			nums1_right = nums1[i] if i < m else float('inf')
			nums2_left = nums2[j - 1] if j > 0 else float('-inf')
			nums2_right = nums2[j] if j < n else float('inf')
			# 符合标准
			if nums1_left <= nums2_right and nums2_left <= nums1_right:
				if (m + n) % 2 == 1:
					return float(max(nums1_left, nums2_left))
				else:
					return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
			elif nums1_left > nums2_right:
				right = i - 1
			else:
				left = i + 1


