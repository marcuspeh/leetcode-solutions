class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))
        result = 0
        maxNumber = -1001
        
        for left, right in pairs:
            if maxNumber < left:
                result += 1
                maxNumber = right
        
        return result