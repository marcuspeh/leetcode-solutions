class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        cache = set()
        minNum = float("inf")
        maxNum = float("-inf")
        for num in nums:
            cache.add(num)
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
        
        result = []
        for num in range(minNum, maxNum + 1):
            if num not in cache:
                result.append(num)
        
        return result