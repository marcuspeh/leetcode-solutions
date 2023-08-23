class Solution:
    def reorganizeString(self, s: str) -> str:
        cache = {}
        maxDuplicate = 0
        for word in s:
            if word not in cache:
                cache[word] = 0
            cache[word] += 1
            maxDuplicate = max(maxDuplicate, cache[word])
            
        if maxDuplicate > len(s) // 2 + len(s) % 2:
            return ""
        
        heap = []
        for key, value in cache.items():
            heapq.heappush(heap, (-value, key))
            
        result = []
        prev = None
        while heap:
            count, word = heapq.heappop(heap)
            result.append(word)
            count += 1
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            if count == 0:
                continue
            
            prev = (count, word)
            
        if prev:
            result.append(prev[1])
        
        return "".join(result)