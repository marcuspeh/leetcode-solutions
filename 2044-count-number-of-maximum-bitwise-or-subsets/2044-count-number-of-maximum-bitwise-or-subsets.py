class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        cache = {}
        for num in nums:
            newCache = {}
            for count, n in cache.items():
                if count not in newCache:
                    newCache[count] = 0
                newCache[count] += n

                newCount = count | num
                if newCount not in newCache:
                    newCache[newCount] = 0
                newCache[newCount] += n
        
            if num not in newCache:
                newCache[num] = 0
            newCache[num] += 1

            cache = newCache
        
        return cache[max(cache.keys())]