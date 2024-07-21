class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        vertical = self.getTopo(rowConditions, k)
        horizontal = self.getTopo(colConditions, k)
        
        if len(vertical) != len(horizontal) or len(horizontal) != k:
            return []
        result = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if vertical[i] != horizontal[j]:
                    continue
                result[i][j] = vertical[i]
        return result
                
        
    def getSequence(self, seq, k):
        nextItem = {}
        noPrev = set(i for i in range(1, k + 1))
        for before, after in seq:
            if before not in nextItem:
                nextItem[before] = set()
            nextItem[before].add(after)
            if after in noPrev:
                noPrev.remove(after)
        return nextItem, noPrev

    def getTopo(self, seq, k):
        seqMap, noPrev = self.getSequence(seq, k)
        stack = []
        color = [0 for i in range(k + 1)]
        cycle = False
        
        def helper(curr):
            nonlocal stack, color, cycle
            if color[curr] == 1:
                cycle = True
            if color[curr] == 2 or cycle:
                return 
            
            color[curr] = 1
            if curr in seqMap:
                for nextCurr in seqMap[curr]:
                    helper(nextCurr)
                    if cycle:
                        return
            color[curr] = 2
            stack.append(curr)
        
        for node in noPrev:
            helper(node)
        if cycle:
            return []
        return stack[::-1]
        
            
                