class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heapq.heappush(heap, -gift)
        
        for _ in range(k):
            largest = -heapq.heappop(heap)
            left = math.floor(math.sqrt(largest))
            heapq.heappush(heap, -left)
        
        total = 0
        for gift in heap:
            total += -gift
        return total
