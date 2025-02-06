


"""
	There are n cities. Some of them are connected, while some are not. 
	If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

	A province is a group of directly or indirectly connected cities and no other cities outside of the group.

	You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

	Return the total number of provinces.

	 

	Example 1:


	Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
	Output: 2
	Example 2:


	Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
	Output: 3
"""

class UnionFind: 
    def __init__(self, size) : 
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def _find(self,x ) -> int: 
        return self.root[x]
    
    def _union(self, x , y) -> None :
        rootA = self._find(x)
        rootB = self._find(y)
        if rootA != rootB : 
            for i in range(len(self.root) ): 
                if self.root[i] == rootB: 
                    self.root[i] = rootA
    
    def _is_connected(self, x , y) -> bool :
        return self.root[x] == self.root[y]


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n): 
            for j in range(i+1, n) :
                if isConnected[i][j] == 1: 
                    uf._union(i, j) 
        
        return len(list(set(uf.root)))


if __name__ == "__main__" : 
	print("TEST 1: ")
	print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))

	print("\n\nTEST 2: ")
	print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))