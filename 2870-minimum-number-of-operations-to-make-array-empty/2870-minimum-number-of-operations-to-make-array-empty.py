class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
        result = 0
        for count in counter.values():
            operations = self.getOperations(count)
            
            if operations == -1:
                return -1
            
            result += operations
            
        return result
    
    def getOperations(self, count):
        if count == 1:
            return -1
    
        result = count // 3
        if count % 3 != 0:
            result += 1
        return result
            
        