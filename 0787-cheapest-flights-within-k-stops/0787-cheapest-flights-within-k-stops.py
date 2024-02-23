class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf') for _ in range(n)]
        cost[src] = 0;
        for _ in range(k + 1):
            temp = cost.copy()
            for origin, destination, price in flights:
                if cost[origin] == float('inf'):
                    continue
                temp[destination] = min(temp[destination], cost[origin] + price)
            cost = temp
        if cost[dst] == float("inf"):
            return -1
        
        return cost[dst]