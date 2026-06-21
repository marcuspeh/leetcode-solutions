class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total = 0
        heap = []
        for cost in costs:
            heapq.heappush(heap, -cost)
            total += cost
            while total > coins:
                tooEx = heapq.heappop(heap)
                total += tooEx
        
        return len(heap)