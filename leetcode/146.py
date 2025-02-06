


"""
	Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

	Implement the LRUCache class:

	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	- int get(int key) Return the value of the key if the key exists, otherwise return -1.
	- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from 
	this operation, evict the least recently used key.
	The functions get and put must each run in O(1) average time complexity.

	Example 1:

	Input
	["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
	[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
	Output
	[null, null, null, 1, null, -1, null, -1, 3, 4]

	Explanation
	LRUCache lRUCache = new LRUCache(2);
	lRUCache.put(1, 1); // cache is {1=1}
	lRUCache.put(2, 2); // cache is {1=1, 2=2}
	lRUCache.get(1);    // return 1
	lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
	lRUCache.get(2);    // returns -1 (not found)
	lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
	lRUCache.get(1);    // return -1 (not found)
	lRUCache.get(3);    // return 3
	lRUCache.get(4);    // return 4
"""

class DoublyLinkedList : 
	def __init__(self,val, prev = None , next = None) : 
		self.val = val 
		self.prev = prev 
		self.next = next

class LRUCache:
	def __init__(self, capacity: int):
		self.capacity = 0
		self.max_capacity = capacity
		self.head = None 
		self.tail = None

	def get(self, key: int) -> int:
		# Edge case: if length is 0 or 1 then 
		if self.capacity <= 0 : return -1 
		if self.capacity == 1 : 
			if self.head.val[0] != key : 
				return -1 
			else:  return self.head.val[1]
		
		pointer = self.head
		while pointer : 
			# After getting the node, this node will be come most recent

			if pointer.val[0] == key : 
				recent_node = pointer		

				# If node is at head 
				if pointer.val[0] == self.head.val[0] : 
					return pointer.val[1]

				# If node is at the tail
				if pointer.val[0] == self.tail.val[0]: 
					self.tail = self.tail.prev 
					self.tail.next = None
					new_node = DoublyLinkedList([recent_node.val[0], recent_node.val[1]], None, self.head)
					self.head = new_node
					self.head.next.prev = self.head

				# If the node is in the middle
				if pointer.val[0] != self.head.val[0] and pointer.val[0] != self.tail.val[0]:
					temp_next = recent_node.next
					recent_node.prev.next = temp_next 
					
					new_node = DoublyLinkedList([recent_node.val[0], recent_node.val[1]], None, self.head)
					self.head = new_node
					self.head.next.prev = self.head

				return pointer.val[1]
			pointer = pointer.next
		return -1 

	def put(self, key: int, value: int) -> None:

		if self.capacity == self.max_capacity and self.max_capacity > 1 : 
			self.tail = self.tail.prev 
			self.tail.next = None 
			self.capacity -=1 		
		if  self.capacity == self.max_capacity and self.max_capacity == 1: 
			self.head = DoublyLinkedList([key,value] , None, None)
			self.tail = self.head
			return

		# If there is no element in list then easy 
		if self.capacity <= 0 : 
			self.head = DoublyLinkedList([key, value], None, None)
			self.tail = self.head
		else : 
			new_node = DoublyLinkedList([key,value] , None, self.head)
			self.head = new_node
			self.head.next.prev = self.head
		self.capacity += 1 	
		return

	def _print_lru(self) -> None : 
		pointer = self.head 
		while pointer : 
			print(pointer.val , end = '>')
			pointer = pointer.next 
		return



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__" : 
	# commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
	# args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

	# # Initialize the cache
	# cache = None
	# output = []

	# for i, command in enumerate(commands):
	# 	if command == "LRUCache":
	# 		cache = LRUCache(args[i][0])
	# 		output.append(None)
	# 	elif command == "put":
	# 		cache.put(args[i][0], args[i][1])
	# 		output.append(None)
	# 	elif command == "get":
	# 		result = cache.get(args[i][0])
	# 		output.append(result)

	# # Expected output: [null, null, null, 1, null, -1, null, -1, 3, 4]
	# print(output)

	lru = LRUCache(2)

	print(lru.get(2)) 
	print(lru.put(2,6))
	print(lru.get(1))
	print(lru.put(1,5))
	print(lru.put(1,2))
	lru._print_lru()
	print(lru.get(1))
	print(lru.get(2))






