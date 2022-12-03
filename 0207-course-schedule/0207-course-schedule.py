class Solution:    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE = 0
        RED = 1
        BLACK = 2
        adjList = {}
        
        for start, end in prerequisites:
            if start not in adjList:
                adjList[start] = []
            adjList[start].append(end)
        
        cache = [WHITE for i in range(numCourses)]
        
        def dfs(currCourse):
            nonlocal cache
            
            if cache[currCourse] == RED:
                return False
            if cache[currCourse] == BLACK:
                return True
            
            cache[currCourse] = RED
            result = True
            
            if currCourse in adjList:
                for end in adjList[currCourse]:
                    result = result and dfs(end)
                    if not result:
                        break
            
            cache[currCourse] = BLACK
            return result
        
        for i in range(numCourses):
            isValid = dfs(i)
            if not isValid:
                return False
        return True