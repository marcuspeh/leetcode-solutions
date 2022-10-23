class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        cache = set()
        missing = set()

        for i in range(1, len(nums) + 1):
            missing.add(i)

        for i in nums:
            if i in cache:
                result.append(i)
                continue

            cache.add(i)
            missing.remove(i)
        
        result.extend(missing)
        return result
