class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = sum(piles)
        
        while start < end:
            mid = start + (end - start) // 2
            if not self.canFinish(piles, mid, h):
                start = mid + 1
            else:
                end = mid
        return start
        
    def canFinish(self, piles, k, h):
        time = 0
        for pile in piles:
            time += ceil(pile / k)
            if time > h:
                return False
        return True