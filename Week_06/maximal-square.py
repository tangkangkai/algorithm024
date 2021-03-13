class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square = 0
        
        new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            new_matrix[i][0] = int(matrix[i][0])
            
            if not max_square and matrix[i][0] == "1":
                max_square = 1
        
        for i in range(len(matrix[0])):
            new_matrix[0][i] = int(matrix[0][i])

            if not max_square and matrix[0][i] == "1":
                max_square = 1
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    new_matrix[i][j] = min(new_matrix[i - 1][j - 1], new_matrix[i][j - 1], new_matrix[i - 1][j]) + 1
                    max_square = max(max_square, new_matrix[i][j])
                    
        return max_square * max_square
                    
                    
                    