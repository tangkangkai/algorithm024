class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        uf = UnionFind(m * n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    uf.count -= 1
                else:
                    if self.get_num(grid, i - 1, j) == "1":
                        uf.union(self.get_index(i, j, n), self.get_index(i - 1, j, n))
                        
                    if self.get_num(grid, i + 1, j) == "1":
                        uf.union(self.get_index(i, j, n), self.get_index(i + 1, j, n))
                        
                    if self.get_num(grid, i, j - 1) == "1":
                        uf.union(self.get_index(i, j, n), self.get_index(i, j - 1, n))
                        
                    if self.get_num(grid, i, j + 1) == "1":
                        uf.union(self.get_index(i, j, n), self.get_index(i, j + 1, n))
        
        return uf.count
        
    def get_num(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            return grid[i][j]
        return None
    
    def get_index(self, i, j, n):
        return i * n + j
        
                
        
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
        
        while self.parent[i] != root:
            x = self.parent[i]
            self.parent[i] = root
            i = x
        
        return root
        