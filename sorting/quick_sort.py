






def quick_sort(lo , hi) : 

	if lo < hi : 
		j = partition(lo, hi) 
		quick_sort(lo, j) 
		quick_sort(j+1 , hi)
	return


def partition(lo, hi):
    pivot = unsorted_array[lo]
    i = lo + 1
    j = hi

    while True:
        while i <= hi and unsorted_array[i] <= pivot:
            i += 1
        while j > lo and unsorted_array[j] > pivot:
            j -= 1

        if i < j:
            unsorted_array[i], unsorted_array[j] = unsorted_array[j], unsorted_array[i]
        else:
            break

    unsorted_array[lo], unsorted_array[j] = unsorted_array[j], unsorted_array[lo]
    return j

if __name__ == "__main__":
    unsorted_array = [34, 7, 23, 32, 5, 62, 11, 19, 25, 8]
    quick_sort(0, len(unsorted_array) - 1)
    print(unsorted_array)  # Print the sorted array
