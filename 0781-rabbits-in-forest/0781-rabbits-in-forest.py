class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        colorMap = {}
        result = 0
        for ans in answers:
            if ans not in colorMap:
                result += ans + 1
                if ans > 0:
                    colorMap[ans] = 0
                continue
            
            colorMap[ans] += 1
            if colorMap[ans] == ans:
                del colorMap[ans]
        
        return result
