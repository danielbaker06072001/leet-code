



"""
	There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D 
	integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. 
	Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

	You want to determine if there is a valid path that exists from vertex source to vertex destination.

	Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

	 

	Example 1:


	Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
	Output: true
	Explanation: There are two paths from vertex 0 to vertex 2:
	- 0 → 1 → 2
	- 0 → 2
	Example 2:


	Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
	Output: false
	Explanation: There is no path from vertex 0 to vertex 5.
"""

class Solution : 

	def validPath(self, n: int, edges : list[list[int]], source: int, destination: int) -> bool:
		self.root = [i for i in range(n)]
		self.rank = [1 for i in range(n)]

		for points in edges: 
			self._union(points[0], points[1])

		return self._is_union(source, destination)	

	def _find(self, x) -> int :
		if x == self.root[x]: return x
		self.root[x] = self._find(self.root[x]) 
		return self.root[x]

	def _union(self, x, y) :
		rootA = self._find(x)
		rootB = self._find(y)
		if rootA != rootB : 
			self.root[rootB] = rootA

	def _is_union(self, x, y) -> bool : 
		return self._find(x) == self._find(y)



if __name__ == "__main__" : 
	print("Test case # 1: ")	
	print(Solution().validPath(3, [[0,1],[1,2],[2,0]], 0, 2))

	print("Test case # 2: ")	
	print(Solution().validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))



















