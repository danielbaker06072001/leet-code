




"""

Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0
"""

class Solution: 
	def threeSumSmaller(self, nums : list, target: int) -> int: 
		

if __name__ == "__main__": 
	arr = [3,6,9,1]
	result = Solution().maximumGap(arr)
	print(result)