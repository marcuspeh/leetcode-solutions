class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cache = [1]
        for idx in range(1, len(strs[0])):
            curr = 1
            for currIdx in range(idx - 1, -1, -1):
                isInOrder = True
                for string in strs:
                    if string[currIdx] <= string[idx]:
                        continue

                    isInOrder = False
                    break 
                
                if not isInOrder:
                    continue
                
                curr = max(curr, cache[currIdx] + 1)
            
            cache.append(curr)
        
        return len(strs[0]) - max(cache)
                