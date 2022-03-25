class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]
        visitedCount = 0
        
        frontier = [0]
        
        while frontier:
            room = frontier.pop()
            
            if visited[room]:
                continue
                
            visited[room] = True
            visitedCount += 1
            
            frontier.extend(rooms[room])
            
        
        
        return visitedCount == len(rooms)