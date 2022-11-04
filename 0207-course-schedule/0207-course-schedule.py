class Solution:
    WHITE = 0
    RED = 1
    BLACK = 2
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        links = {}
        noEntry = {i for i in range(numCourses)}
        
        for i, j in prerequisites:
            if j not in links:
                links[j] = []
            links[j].append(i)
            if i in noEntry:
                noEntry.remove(i)
    
        colors = [self.WHITE for _ in range(numCourses)]
        visited = set()
        
        for node in noEntry:
            isValid = self.dfs(links, colors, node, visited)
            if not isValid:
                return False
            
        return len(visited) == numCourses
        
    def dfs(self, links, colors, curr, visited):
        if curr in visited:
            return True
        
        if colors[curr] == self.RED:
            return False
        
        colors[curr] = self.RED
        if curr in links:
            for nextNode in links[curr]:
                isValid = self.dfs(links, colors, nextNode, visited)
                if not isValid:
                    return False
        colors[curr] = self.BLACK
        visited.add(curr)
        return True
        