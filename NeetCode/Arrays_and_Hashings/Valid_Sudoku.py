# The following code is for the Valid Sudoku problem on leetcode.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        return (self.is_row_valid(board) and 
                self.is_col_valid(board) and 
                self.is_box_valid(board))
    
    def is_row_valid(self, board):
        for row in board:
            if not self.is_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_valid(col):
                return False
        return True

    def is_box_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid(square):
                    return False
        return True
    
    def is_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
