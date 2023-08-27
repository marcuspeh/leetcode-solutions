class Solution:
    def canCross(self, stones: List[int]) -> bool:
        table = [[False for _ in range(2001)] for _ in range(2001)]
        table[0][0] = True
        
        mark = {}
        for i in range(len(stones)):
            mark[stones[i]] = i
        
        for i in range(len(stones)):
            for jump in range(len(stones) + 1):
                if not table[i][jump]:
                    continue
                    
                if stones[i] + jump - 1 in mark:
                    table[mark[stones[i] + jump - 1]][jump - 1] = True
                if stones[i] + jump in mark:
                    table[mark[stones[i] + jump]][jump] = True
                if stones[i] + jump + 1 in mark:
                    table[mark[stones[i] + jump + 1]][jump + 1] = True
                    
        for i in range(len(stones) + 1):
            if table[len(stones) - 1][i]:
                return True
        return False