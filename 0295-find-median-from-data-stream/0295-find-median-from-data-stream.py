class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.right, num)
        num = heapq.heappop(self.right)
        heapq.heappush(self.left, -num)
        
        if len(self.left) > len(self.right) + 1:
            temp = -heapq.heappop(self.left)
            heapq.heappush(self.right, temp)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return - self.left[0]
        return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()