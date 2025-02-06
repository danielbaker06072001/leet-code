



def insertion_sort(arr):
	n = len(arr)  
	for i in range(1,n) : 
		for j in range(i, 0 , -1) : 
			if less_than(arr[j], arr[j - 1]): 
				arr = swap(arr, j , j-1)
	return arr

def less_than(i , j) :
	return i < j 

def swap(arr, i, j ) : 
    temp = arr[i]
    arr[i], arr[j] = arr[j], temp
    return arr


if __name__ == "__main__" : 
    unsorted_array = [34, 7, 23, 32, 5, 62, 11, 19, 25, 8]
    sorted_arr = insertion_sort(unsorted_array)
    print(sorted_arr)



