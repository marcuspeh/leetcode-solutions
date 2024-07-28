class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        D = [[] for _ in range(n + 1)]
        D[1] = [0]
        G, heap = defaultdict(list), [(0, 1)]
        
        for a, b in edges:
            G[a] += [b]
            G[b] += [a]

        while heap:
            min_dist, idx = heappop(heap)
            if idx == n and len(D[n]) == 2: return max(D[n])

            for neib in G[idx]:
                cand = self.getNextCost(min_dist, time, change)

                if not D[neib] or (len(D[neib]) == 1 and D[neib] != [cand]):
                    D[neib] += [cand]
                    heappush(heap, (cand, neib))
        return -1
    
    def getNextCost(self, cost, time, change):
        temp = cost // change
        if temp % 2 == 0:
            return cost + time 
        return change * (temp + 1) + time

