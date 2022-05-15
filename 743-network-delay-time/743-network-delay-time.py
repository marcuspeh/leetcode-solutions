import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        pq = [(0, k)]
        edges = {}
        time = 0
        
        for u, v, w in times:
            if u not in edges:
                edges[u] = []
                
            edges[u].append((v, w))
        
        while pq:
            cost, node = heapq.heappop(pq)
            
            if node in visited:
                continue
            
            time = cost
            
            visited.add(node)
            
            if node in edges:
                for v, w in edges[node]:
                    heapq.heappush(pq, (cost + w, v))
                
        if len(visited) == n:
            return time
        else:
            return -1
            