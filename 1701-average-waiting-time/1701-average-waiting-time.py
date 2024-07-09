class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currentTime = 0
        totalWait = 0
        
        for arrival, time in customers:
            currWait = max(currentTime - arrival, 0) + time
            currentTime = max(currentTime, arrival) + time
            totalWait += currWait
        return totalWait / len(customers)