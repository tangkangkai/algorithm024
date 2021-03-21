class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        column = [{} for _ in range(9)]
        section = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                
                if value == ".":
                    continue
                
                int_value = int(value)
                
                # judge row
                if int_value in row[i] and row[i][int_value]:
                    return False
                row[i][int_value] = 1
                
                # judge column
                if int_value in column[j] and column[j][int_value]:
                    return False
                column[j][int_value] = 1
                
                # judge section
                section_i = (i // 3) * 3 + j // 3
                
                if int_value in section[section_i] and section[section_i][int_value]:
                    return False
                
                section[section_i][int_value] = 1
                
        return True