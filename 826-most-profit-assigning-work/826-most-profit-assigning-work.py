class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        task = sorted(zip(difficulty, profit), key=lambda x: x[1], reverse=True)
        worker.sort()
        
        result = 0
        workerRemaining = len(worker)
        
        for i in task:
            diff, money = i
            
            index = self.binarySearch(worker, workerRemaining - 1, diff)
            
            if index < workerRemaining:
                result += money * (workerRemaining - index)
                workerRemaining = index
        
        return result
            
    def binarySearch(self, arr, right, n):
        left = 0
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] < n:
                left = mid + 1
            else:
                right = mid 
        
        return left if arr[left] >= n else right + 1
        