import heapq

class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []
        
    def addNum(self, num: int) -> None:
        heappush(self.smaller, -num)
        toInsert = -heappop(self.smaller)
        
        heappush(self.larger, toInsert)
        
        if len(self.larger) > len(self.smaller) + 1:
            toInsert = heappop(self.larger)
            heappush(self.smaller, -toInsert)

    def findMedian(self) -> float:
        if len(self.larger) == len(self.smaller) + 1:
            return self.larger[0]
    
        return (-self.smaller[0] + self.larger[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()