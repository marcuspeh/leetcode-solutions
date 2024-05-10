class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = [(arr[0] / arr[len(arr) - 1], 0, len(arr) - 1)]
        seen = {(0, len(arr) - 1)}
        
        for i in range(k - 1):
            _, start, end = heapq.heappop(heap)
            
            if start + 1 < end and (start + 1, end) not in seen:
                seen.add((start + 1, end))
                heapq.heappush(heap, (arr[start + 1] / arr[end], start + 1, end))
            if start < end - 1 and (start, end - 1) not in seen:
                seen.add((start, end - 1))
                heapq.heappush(heap, (arr[start] / arr[end - 1], start, end - 1))         
            
        _, start, end = heapq.heappop(heap)
        return (arr[start], arr[end])