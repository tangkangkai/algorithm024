class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        length = 9
        
        row_set = collections.defaultdict(set)
        column_set = collections.defaultdict(set)
        section_set = collections.defaultdict(set)
        empty = collections.deque([])
        
        for i in range(length):
            for j in range(length):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    int_val = int(board[i][j])
                    row_set[i].add(int_val)
                    column_set[j].add(int_val)
                    section_set[(i // 3, j // 3)].add(int_val)
        
        return self.dfs(board, row_set, column_set, section_set, empty)
        
        
    def dfs(self, board, row_set, column_set, section_set, empty):
        if not empty:
            return True
        
        row, column = empty[0]
        
        for i in range(1, 10):
            if i not in row_set[row] and i not in column_set[column] and i not in section_set[(row // 3, column // 3)]:
                board[row][column] = str(i)
                row_set[row].add(i)
                column_set[column].add(i)
                section_set[(row // 3, column // 3)].add(i)
                empty.popleft()
            
                if self.dfs(board, row_set, column_set, section_set, empty):
                    return True
                else:
                    row_set[row].remove(i)
                    column_set[column].remove(i)
                    section_set[(row // 3, column // 3)].remove(i)
                    empty.appendleft((row, column))
        
        
        return False