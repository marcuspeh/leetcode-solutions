class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        busAtStop = {}
        
        for bus in range(len(routes)):
            route = routes[bus]
            
            for currStop in route:
                if currStop not in busAtStop:
                    busAtStop[currStop] = set()
                busAtStop[currStop].add(bus)
                
        frontier = [(source, 0)] # location, steps
        visited = set([source])
        
        while frontier:
            currBusStop, busChanges = frontier.pop(0)
            
            for bus in busAtStop[currBusStop]:
                
                for stop in routes[bus]:
                    if stop in visited:
                        continue
                        
                    if stop == target:
                        return busChanges + 1
                    else:
                        frontier.append((stop, busChanges + 1))
                        visited.add(stop)
                routes[bus] = []
                        
        return -1
       