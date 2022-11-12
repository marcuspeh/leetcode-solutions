import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        toShift = heapq.heappop(self.small)
        heapq.heappush(self.big, -toShift)
        
        if len(self.small) + 1 < len(self.big):
            toShift = heapq.heappop(self.big)
            heapq.heappush(self.small, -toShift)
            

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return (-self.small[0] + self.big[0]) / 2
        return self.big[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()