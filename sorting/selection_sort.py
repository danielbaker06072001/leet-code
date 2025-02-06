


"""
    Selection sort: iterate through array, find the smallest value then swap 
    Time complexity: O(n^2)
"""

def selection_sort(arr: list ) -> list: 
    n = len(arr) 
    for curr_minimum in range(n) : 
        for curr_item in range(curr_minimum, n) : 
            if arr[curr_item] < arr[curr_minimum]:
                arr = swap(arr, curr_minimum, curr_item)

    return arr

def swap(arr, i, j ) : 
    temp = arr[i]
    arr[i], arr[j] = arr[j], temp
    return arr



if __name__ == "__main__" : 
    unsorted_array = [34, 7, 23, 32, 5, 62, 11, 19, 25, 8]
    sorted_arr = selection_sort(unsorted_array)
    print(sorted_arr)



