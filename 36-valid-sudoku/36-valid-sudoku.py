class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRow(board) and self.checkCol(board) and self.checkSquare(board)
        
    def checkRow(self, board):
        for i in board:
            temp = set()
            for j in i:
                if j == ".":
                    continue
                    
                if j in temp:
                    return False
                else:
                    temp.add(j)
        return True
    
    def checkCol(self, board):
        for i in range(len(board)):
            temp = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                    
                if board[j][i] in temp:
                    return False
                else:
                    temp.add(board[j][i])
        return True
    
    
    def checkSquare(self, board):
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                temp = set()
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y] == ".":
                            continue
                        if board[i + x][j + y] in temp:
                            return False
                        else:
                            temp.add(board[i + x][j + y])
        return True
        
       