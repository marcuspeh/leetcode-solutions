class Solution:
    UNGUARDED = 0
    GUARDED = 1
    WALL = 2
    GUARD = 3

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        table = [[self.UNGUARDED] * n for _ in range(m)]
        for i, j in guards:
            table[i][j] = self.GUARD

        for i, j in walls:
            table[i][j] = self.WALL
        
        for i, j in guards:
            self.fillGuarded(i, j, table)

        result = 0
        for row in table:
            for col in row:
                if col == self.UNGUARDED:
                    result += 1

        return result

    def fillGuarded(self, i, j, table):
        for x in range(j - 1, -1, -1):
            if table[i][x] == self.WALL or table[i][x] == self.GUARD:
                break
            table[i][x] = self.GUARDED
            
        for x in range(j + 1, len(table[0])):
            if table[i][x] == self.WALL or table[i][x] == self.GUARD:
                break
            table[i][x] = self.GUARDED

        for y in range(i - 1, -1, -1):
            if table[y][j] == self.WALL or table[y][j] == self.GUARD:
                break
            table[y][j] = self.GUARDED

        for y in range(i + 1, len(table)):
            if table[y][j] == self.WALL or table[y][j] == self.GUARD:
                break
            table[y][j] = self.GUARDED