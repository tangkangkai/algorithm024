class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []
        self.backtrack(res, curr, n, k, 1)
        
        return res
        
    def backtrack(self, res, curr, n, k, start):
        if len(curr) == k:
            res.append(curr[::])
            return
        
        for i in range(start, n + 1):
            curr.append(i)
            self.backtrack(res, curr, n, k, i + 1)
            curr.pop()
        
        
        
        
        