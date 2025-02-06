from heapq import heappush, heappop
import heapq


if __name__ == "__main__": 
	heap = [1,5,1,23,7,4,5,6,2]

	heapq.heapify(heap)
	while heap : 
		print(heappop(heap))
	print(heap)