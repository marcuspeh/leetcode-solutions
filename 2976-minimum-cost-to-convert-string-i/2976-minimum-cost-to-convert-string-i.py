class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        changes = {}
        for i in range(len(original)):
            before = original[i]
            after = changed[i]
            val = cost[i]
            
            if before not in changes:
                changes[before] = {}
            if after not in changes[before]:
                changes[before][after] = float("inf")
            changes[before][after] = min(changes[before][after], val)

        cache = {}
        for i in range(26):
            character = chr(ord('a') + i)
            if character not in changes:
                continue
            cache[character] = self.dijkstra(character, changes)
        
        result = 0
        for i in range(len(source)):
            currChar = source[i]
            newChar = target[i]
            
            if currChar == newChar:
                continue
            if currChar not in cache:
                return -1
            if newChar not in cache[currChar]:
                return -1
            result += cache[currChar][newChar]
        return result
        
    def dijkstra(self, startCharacter, changes):
        costMap = {}
        
        heap = [(0, startCharacter)]
        while heap:
            cost, char = heapq.heappop(heap)
            if char in costMap:
                continue
            costMap[char] = cost
            
            if char not in changes:
                continue
            for nextChar, nextCost in changes[char].items():
                if nextChar in costMap:
                    continue
                heapq.heappush(heap, (cost + nextCost, nextChar))
        return costMap