class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ringIdx = {} # g[0, 6], o[1], d[2, 3], i[4], n[5]
        for i in range(len(ring)):
            word = ring[i]
            if word not in ringIdx:
                ringIdx[word] = []
            ringIdx[word].append(i)
            
        frontier = [(0, 0, 0)] # steps, -keyIdx, currIdx
        visited = set()
        while frontier:
            steps, keyIdx, currIdx = heapq.heappop(frontier)
            if -keyIdx >= len(key):
                return steps
            if (keyIdx, currIdx) in visited:
                continue
            visited.add((keyIdx, currIdx))

            nextKeyWord = key[-keyIdx]
            for newIdx in ringIdx[nextKeyWord]:
                if (keyIdx - 1, newIdx) in visited:
                    continue
                newSteps = self.indexAway(len(ring), newIdx, currIdx) + steps + 1
                heapq.heappush(frontier, (newSteps, keyIdx - 1, newIdx))
        
        return -1
        
    def indexAway(self, length, newIdx, currIdx):
        stepsBtwn = abs(currIdx - newIdx)
        stepsArd = length - stepsBtwn
        return min(stepsBtwn, stepsArd)