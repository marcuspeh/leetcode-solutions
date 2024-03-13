class Solution:
    def getSurroundings(self, board, x, y):
        surrounding = [
            (1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)
        ]
        result = []
        for i, j in surrounding:
            newX = x + i
            newY = y + j
            if newX < 0 or newX >= len(board):
                continue
            if newY < 0 or newY >= len(board[0]):
                continue
            result.append((newX, newY))
        return result
    
    
    def countMines(self, board, cells):
        mines = 0
        for i, j in cells:
            if board[i][j] == "M":
                mines += 1
        return mines
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        
        frontier = [(x, y)]
        while frontier:
            x, y = frontier.pop()
            if board[x][y] != "M" and board[x][y] != "E":
                continue
                
            surrounding = self.getSurroundings(board, x, y)
            minesCount = self.countMines(board, surrounding)
            
            if minesCount > 0:
                board[x][y] = str(minesCount)
                continue
            board[x][y] = 'B'
            frontier.extend(surrounding)
            
        return board