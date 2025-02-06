



"""
	Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

	You must write an algorithm that runs in linear time and uses linear extra space.

	 

	Example 1:

	Input: nums = [3,6,9,1]
	Output: 3
	Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
	Example 2:

	Input: nums = [10]
	Output: 0
	Explanation: The array contains less than 2 elements, therefore return 0.
"""

# This suppose to use Radix / bucket sort, however I don't think I'll need that in the near future

class Solution:
	def maximumGap(self, nums) -> int:
		ans = 0

		if len(nums) <= 1 :
			return 0 

		nums.sort()

		max_gap = abs(nums[0] - nums[1])

		for i in range(1, len(nums)-1) : 
			next_gap = abs(nums[i] - nums[i+1])
			if next_gap > max_gap: max_gap = next_gap

		return max_gap




if __name__ == "__main__": 
	arr = [3,6,9,1]
	result = Solution().maximumGap(arr)
	print(result)