



class DisjointSetQuickFind: 

	def __init__(self, n: int) :
		self.root = [i for i in range(n)]


	def _find(self, vertice) -> int :
		return self.root[vertice]

	def _union(self, x :int, y: int) -> None : 
		rootX = self._find(x)
		rootY = self._find(y)
		if rootX != rootY:
			for i in range(len(self.root)):
				if self.root[i] == rootY:
					self.root[i] = rootX

	def _is_connect(self, vertice1, vertice2) -> bool : 
		return self._find(vertice1) == self._find(vertice2)

	def _print(self): 
		print(self.root)

class DisjointSet: 
	def __init__(self, size) : 
		self.root = [i for i in range(size)]

	def _find(self, x) -> int :
		while x != self.root[x] : 
			x = self.root[x]
		return x

	def _union(self, x, y ): 
		rootA = self._find(x) 
		rootB = self._find(y)
		if rootA != rootB: 
			self.root[rootB] = rootA

	def _is_connect(self, x, y ) : 
		return self._find(x) == self._find(y)

	def _print(self): 
		print(self.root)

class DisjointSetRank: 
	def __init__(self, size) : 
		self.root = [i for i in range(size)]
		self.rank = [1 for i in range(size)]

	def _find(self, x) : 
		while x != self.root[x] : 
			x = self.root[x]
		return x 

	def _union(self, x , y): 
		rootA = self._find(x)
		rootB = self._find(y) 
		if rootA != rootB : 
			if self.rank[rootA] > self.rank[rootB] :
				self.root[rootB] = rootA
			elif self.rank[rootA] < self.rank[rootB]:
				self.root[rootA] = rootB
			else : 
				self.root[rootB] = rootA
				self.rank[rootA] += 1


	def _is_connect(self, x, y ) : 
		return self._find(x) == self._find(y)

	def _print(self): 
		print(self.root)

class DisjointSetCompression: 
	def __init__(self, size) : 
		self.root = [i for i in range(size)]

	def _find(self, x) : 
		if x == self.root[x]:
			return x
		self.root[x] = self._find(self.root[x])
		return self.root[x]

	def _union(self, x , y): 
		rootA = self._find(x)
		rootB = self._find(y) 
		if rootA != rootB : 
			self.root[rootB] = rootA

	def _is_connect(self, x, y ) : 
		return self._find(x) == self._find(y)

	def _print(self): 
		print(self.root)

if __name__ == "__main__": 
	# [[0,1],[0,2],[3,5],[5,4],[4,3]]
	ds = DisjointSetCompression(6)
	ds._union(0,1)
	ds._union(0,2)
	ds._print()
	print(ds._is_connect(1,2))
