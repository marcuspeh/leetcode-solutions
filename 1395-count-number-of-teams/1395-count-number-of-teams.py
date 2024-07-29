class Solution:
    def numTeams(self, rating: List[int]) -> int:
        increasingCount = [0 for _ in rating]
        decreasingCount = [0 for _ in rating]
        result = 0
        for i in range(len(rating)):
            result += self.countIncrease(rating, i, increasingCount)
            result += self.countDecrease(rating, i, decreasingCount)
        return result
            
    def countIncrease(self, rating, n, increasingCount):
        result = 0
        for i in range(n):
            if rating[i] >= rating[n]:
                continue
            result += increasingCount[i]
            increasingCount[n] += 1
        return result
    
    def countDecrease(self, rating, n, decreasingCount):
        result = 0
        for i in range(n):
            if rating[i] <= rating[n]:
                continue
            result += decreasingCount[i]
            decreasingCount[n] += 1
        return result
        
