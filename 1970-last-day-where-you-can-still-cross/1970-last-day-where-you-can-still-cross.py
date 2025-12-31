class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        start = 0
        end = len(cells) - 1
        for i in range(len(cells)):
            cells[i] = (cells[i][0] - 1, cells[i][1] - 1)

        while start < end:
            mid = (end + start) // 2
            cannotCross = set(cells[:mid + 1])
            if self.dfs(row, col, cannotCross):
                start = mid + 1
                continue
            end = mid
        
        return start 
        
    def dfs(self, row, col, cannotCross):
        visited = set()
        frontier = []
        for i in range(col):
            if (0, i) in cannotCross:
                continue
            visited.add((0, i))
            frontier.append((0, i))

        if row == 1 and frontier:
            return True

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while frontier:
            i, j = frontier.pop()
            for changeI, changeJ in moves:
                newI = i + changeI
                newJ = j + changeJ

                if (newI, newJ) in visited:
                    continue
                if (newI, newJ) in cannotCross:
                    continue
                if newI < 0 or newI >= row:
                    continue
                if newJ < 0 or newJ >= col:
                    continue
        
                if newI == row - 1:
                    return True

                frontier.append((newI, newJ))
                visited.add((newI, newJ))
            
        return False
