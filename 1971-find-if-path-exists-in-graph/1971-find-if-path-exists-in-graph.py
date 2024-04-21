class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        paths = {}
        for node1, node2 in edges:
            if node1 not in paths:
                paths[node1] = []
            paths[node1].append(node2)
        
            if node2 not in paths:
                paths[node2] = []
            paths[node2].append(node1)
        
        frontier = [source]
        visited = {source}
        while frontier:
            node = frontier.pop()
            
            if node not in paths:
                continue
                
            for nextNode in paths[node]:
                if nextNode in visited:
                    continue
                if nextNode == destination:
                    return True
                visited.add(nextNode)
                frontier.append(nextNode)

        return False
                
            
            