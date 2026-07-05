class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10 ** 9 + 7
        OBSTACLE = "X"
        table = [[(float('-inf'), float("-inf")) for _ in row] for row in board]
        table[0][0] = (1, 0)
        for i in range(1, len(board)):
            if board[i][0] == OBSTACLE:
                continue

            prevPath, prevCost = table[i - 1][0]
            table[i][0] = (prevPath, prevCost + int(board[i][0]))

        for j in range(1, len(board[0])):
            if board[0][j] == OBSTACLE:
                continue

            prevPath, prevCost = table[0][j - 1]
            table[0][j] = (prevPath, prevCost + int(board[0][j]))
        
        for i in range(1, len(board)):
            for j in range(1, len(board[0])):
                if board[i][j] == OBSTACLE:
                    continue
                
                prevPath1, prevCost1 = table[i - 1][j]
                prevPath2, prevCost2 = table[i][j - 1]
                prevPath3, prevCost3 = table[i - 1][j - 1]

                if prevPath1 == prevPath2 == prevPath3 == float("-inf"):
                    continue
                
                newCost = max(prevCost1, prevCost2, prevCost3) 
                newPath = 0
                if prevPath1 != float("-inf") and prevCost1 == newCost:
                    newPath += prevPath1
                if prevPath2 != float("-inf") and prevCost2 == newCost:
                    newPath += prevPath2 
                if prevPath3 != float("-inf") and prevCost3 == newCost:
                    newPath += prevPath3
            
                if board[i][j] != 'S':
                    newCost += int(board[i][j])
                table[i][j] = (newPath % MOD, newCost % MOD)

        if table[-1][-1][0] == float("-inf"):
            return (0, 0)
        path, cost = table[-1][-1]
        return cost, path