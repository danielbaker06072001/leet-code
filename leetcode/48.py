



"""
	48. Rotate Image
	Medium
	Topics
	Companies
	You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

	You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
	 
	Example 1:

	Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
	Output: [[7,4,1],[8,5,2],[9,6,3]]
	Example 2:


	Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
	Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

"""

# Approach: 
# 	think of this like we're having boundires on 4 edge, left, right, bottom and top , this will allow us to move element
#	We will move the corner first, then the edge can be move using off-set to the corner (also using pointer to check what layer it's in)

class Solution:
	def rotate(self, matrix : list) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""

		





if __name__ == "__main__":
	solution = Solution()

	# Test case 1
	print("____________PRINTING RESULT TEST 1 ___________________")
	matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
	print(matrix1)
	solution.rotate(matrix1)
	print(matrix1)  # Output: [[7,4,1],[8,5,2],[9,6,3]]

	# Test case 2
	print("\n\n____________PRINTING RESULT TEST 2___________________")
	matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
	print(matrix2)
	solution.rotate(matrix2)
	print(matrix2)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]