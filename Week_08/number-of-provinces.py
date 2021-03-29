class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and i != j:
                    uf.union(i, j)
        
        return uf.count
        
        
class UnionFind:
    def __init__(self, num):
        self.parent = [i for i in range(num)]
        self.count = num
        
    def union(self, i, j):
        p = self.find_parent(i)
        q = self.find_parent(j)
        
        if p != q:
            self.parent[p] = q
            self.count -= 1
        
    def find_parent(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[i] != i:
            x = self.parent[i]
            self.parent[i] = root
            i = x
        return root