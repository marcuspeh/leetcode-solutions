class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        cache = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in cache:
                cache[groupSizes[i]] = []
            cache[groupSizes[i]].append(i)
            
        result = []
        for key, values in cache.items():
            for i in range(0, len(values), key):
                result.append(values[i : i + key])
        return result