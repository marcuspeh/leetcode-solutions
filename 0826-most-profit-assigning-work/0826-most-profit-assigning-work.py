class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profits: List[int], workers: List[int]) -> int:
        difficulty = [(difficulty[i], i) for i in range(len(difficulty))]
        difficulty.sort()
        workers.sort()
        
        highestProfit = 0
        result = 0
        i = 0
        
        for worker in workers:
            while i < len(difficulty) and difficulty[i][0] <= worker:
                highestProfit = max(highestProfit, profits[difficulty[i][1]])
                i += 1
            result += highestProfit
        
        return result