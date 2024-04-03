class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, index):
            if index == len(word):
                return True
            
            if board[i][j] != word[index]:
                return False
            
            if index == len(word) - 1:
                return True
            
            letter = board[i][j]
            board[i][j] = ""
            
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for changeI, changeJ in direction:
                newI = i + changeI
                newJ = j + changeJ
                
                if newI < 0 or newI >= len(board):
                    continue
                if newJ < 0 or newJ >= len(board[0]):
                    continue
                if dfs(newI, newJ, index + 1):
                    return True
            
            board[i][j] = letter
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
            
            
                