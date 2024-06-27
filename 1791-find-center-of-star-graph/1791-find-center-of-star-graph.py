class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgeCount = {}
        for u, v in edges:
            if u not in edgeCount:
                edgeCount[u] = 0
            edgeCount[u] += 1
            if edgeCount[u] > 2:
                return u
            
            if v not in edgeCount:
                edgeCount[v] = 0
            edgeCount[v] += 1
            if edgeCount[v] > 2:
                return v
        
        highestEdge = edgeCount[1]
        for i, j in edgeCount.items():
            if j <= edgeCount[highestEdge]:
                continue
            highestEdge = i
        return highestEdge
            