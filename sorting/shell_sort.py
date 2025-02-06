

import math
from insertion_sort import insertion_sort

"""
	Initial impelemtation
	It works and produce the correct answer , however it need improvement
"""

def shell_sort(arr):
	n = len(arr) - 1 

	# Step 1: choose the increment sequence, there are 4 different way to define h,
	#		However, using this formular is good : 3x +  1, for all x < 2^x

	# We choose h by 3 * x +  1 
	h = 1
	h_seq = [1]
	while h <= math.ceil(n/3):
		h = 3 * h + 1 
		h_seq.append(h)


	# Loop through the sequence and use them
	for step in range(len(h_seq) - 1, -1, -1): 
		sub_array = [ x for x in range(0, len(arr), h_seq[step] ) ]	

		# insertion sort for sub_array
		for pointerA in range(1, len(sub_array)): 
			for pointerB in range(pointerA, 0 , -1) : 	# Getting value from bottom : 8, 4, 0
				if less_than(arr, sub_array[pointerB] , sub_array[pointerB - 1]):
					arr = swap(arr, sub_array[pointerB], sub_array[pointerB - 1])
	return arr

""" 
	Improvement implementation
	This one is more clean and stick to the concept
"""
def shell_sort_clean(arr) : 
	n = len(arr) 
	# Step 1 : calculate the h value
	h = 1
	h_seq = [1] 
	while h <= math.ceil(n/3):
		h = 3 * h + 1 
		h_seq.append(h)

	# Step 2 : loop through gap sequence and sort subarrays
	for step in range(len(h_seq) - 1 , -1, -1):
		gap = h_seq[step]	# 1 , 4 

		# Perform insertion sort using gap
		for i in range(gap, n) : 
			temp = arr[i]
			j = i
			while j >= gap and arr[j-gap] > temp: 
				arr[j] = arr[j-gap]
				j -= gap
			arr[j] = temp
	return arr


def less_than(arr, i , j) : 
	return arr[i] < arr[j]

def swap(arr, i , j ) : 
	temp = arr[i]
	arr[i], arr[j] = arr[j], temp
	return arr




if __name__ == "__main__" : 
    unsorted_array = [34, 7, 23, 32, 5, 62, 11, 19, 25, 8]
    # sorted_arr = shell_sort(unsorted_array)
    sorted_arr = shell_sort_clean(unsorted_array)
    print(sorted_arr)



