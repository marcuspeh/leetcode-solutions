class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = [{} for _ in range(n)]
        for start, end, cost in edges:
            self.addEdge(start, end, cost, edgeMap)
            self.addEdge(end, start, cost * 2, edgeMap)
        
        visited = [False for _ in range(n)]
        frontier = [(0, 0)]
        while frontier:
            cost, node = heapq.heappop(frontier)
            if visited[node]:
                continue
            visited[node] = True
            if node == n - 1:
                return cost
            
            for nextNode, nextCost in edgeMap[node].items():
                if visited[nextNode]:
                    continue
                heapq.heappush(frontier, (cost + nextCost, nextNode))
        
        return -1
    
    def addEdge(self, start, end, cost, map):
        if end not in map[start]:
            map[start][end] = float('inf')
        
        map[start][end] = min(map[start][end], cost)