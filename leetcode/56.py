




"""
	Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

	Example 1:

	Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
	Output: [[1,6],[8,10],[15,18]]
	Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
	Example 2:

	Input: intervals = [[1,4],[4,5]]
	Output: [[1,5]]
	Explanation: Intervals [1,4] and [4,5] are considered overlapping.
	
"""

class Solution:
	def merge(self, intervals) :
		ans = []
		check = False
		if len(intervals) <= 0 : return
		if len(intervals) == 1 : return intervals

		intervals = sorted(intervals, key = lambda x: x[0])

		current_interval = intervals[0]

		for i in range(1, len(intervals)) : 
			next_interval = intervals[i]

			if self.is_intersect(current_interval, next_interval) : 
				current_interval = [
					min(current_interval[0], next_interval[0]),
					max(current_interval[1], next_interval[1])
				]
			else : 
				ans.append(current_interval)
				current_interval = next_interval
		ans.append(current_interval)
		
		print(ans)
		return


	def is_intersect(self, arr1, arr2) :
		# print(arr1[0] < arr2[0] and arr1[1] < arr2[0])
		return arr1[1] >= arr2[0]

if __name__ == "__main__": 
	intervals = [[1,3],[2,6],[8,10],[15,18]]
	print(Solution().merge(intervals))
