class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        edges = {}
        for x, y, cost in roads:
            if x not in edges:
                edges[x] = []
            edges[x].append((y, cost))
        
            if y not in edges:
                edges[y] = []
            edges[y].append((x, cost))

        result = float('inf')
        frontier = [n]
        visited = set()
        while frontier:
            node = frontier.pop()
            if node not in edges:
                continue

            for newNode, newCost in edges[node]:
                if newNode in visited:
                    continue

                visited.add(node)
                result = min(result, newCost)
                frontier.append(newNode)

        return result
            