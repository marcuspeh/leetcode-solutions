class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        if start == end:
            return 1

        edgeMap = {}
        for i in range(len(edges)):
            node1, node2 = edges[i]
            pr = succProb[i]

            if node1 not in edgeMap:
                edgeMap[node1] = []
            edgeMap[node1].append((node2, pr))

            if node2 not in edgeMap:
                edgeMap[node2] = []
            edgeMap[node2].append((node1, pr))
        
        if start not in edgeMap:
            return 0

        heap = [(-1, start)]
        visited = set()
        while heap:
            pr, node = heapq.heappop(heap)
            pr = -pr

            if node in visited:
                continue
            visited.add(node)
        
            if node == end:
                return pr
            
            for nextNode, nextPr in edgeMap[node]:
                if nextNode in visited:
                    continue
                newPr = pr * nextPr
                heapq.heappush(heap, (-newPr, nextNode))
            
        return 0