class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        table = [[0 for i in range(j)] for j in range(1, 102)]
        
        table[0][0] = poured
        
        for row in range(query_row + 1):
            for col in range(row + 1):
                if table[row][col] > 1:
                    overflow = table[row][col] - 1
                    table[row][col] = 1
                    
                    table[row + 1][col] += overflow / 2
                    table[row + 1][col + 1] += overflow / 2
                    
        
        return min(1.0, table[query_row][query_glass])