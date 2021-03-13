class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        if len(grid) == 1:
            return sum(grid[0])
        
        first, second = grid[0], grid[1]
        
        # process first
        for i in range(1, len(first)):
            first[i] += first[i - 1]
        
        # process the rest
        for i in range(1, len(grid)):
            if i > 1:
                first, second = second, grid[i]
            for j in range(len(second)):
                second[j] += min(first[j], second[j - 1] if j > 0 else first[j])
            
        return second[-1]