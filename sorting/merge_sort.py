


def merge_sort(arr) : 

	if len(arr) <= 1 : return arr 
	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return _merge_sub_array(left,right)

def _merge_sub_array(arr1, arr2) : 

	pointerA, pointerB = 0, 0 
	lenA , lenB = len(arr1), len(arr2) 

	ans = []
	while pointerA < lenA and pointerB < lenB: 
		if arr1[pointerA] < arr2[pointerB]:
			ans.append(arr1[pointerA])
			pointerA += 1
		else :
			ans.append(arr2[pointerB])
			pointerB += 1
	if pointerA < lenA : ans.extend(arr1[pointerA:])
	if pointerB < lenB: ans.extend(arr2[pointerB:])
	return ans


if __name__ == "__main__": 
    unsorted_array = [34, 7, 23, 32, 5, 62, 11, 19, 25, 8]
    sorted_arr = merge_sort(unsorted_array)
    print(sorted_arr)