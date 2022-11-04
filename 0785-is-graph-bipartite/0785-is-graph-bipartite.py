class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        grid = [0 for i in range(len(graph))] 
        
        for i in range(len(graph)):
            if grid[i] != 0:
                continue
                
            grid[i] = 1
            frontier = [i]
            
            while frontier:
                currNode = frontier.pop() 
                
                for j in graph[currNode]: 
                    if grid[j] == 0:
                        grid[j] = 2 if grid[currNode] == 1 else 1
                        frontier.append(j)
                    elif grid[j] == grid[currNode]:
                        return False
        return True