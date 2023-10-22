class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.larger, num)
        num = heapq.heappop(self.larger)
        heapq.heappush(self.smaller, -num)
        
        if len(self.smaller) - 1 > len(self.larger):
            num = heapq.heappop(self.smaller)
            heapq.heappush(self.larger, -num)
        

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.larger):
            return (-self.smaller[0] + self.larger[0]) / 2
        return -self.smaller[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()