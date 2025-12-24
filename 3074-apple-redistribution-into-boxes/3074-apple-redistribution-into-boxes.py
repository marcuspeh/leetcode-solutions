class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        totalApple = sum(apple)
        idx = 0
        while totalApple > 0:
            totalApple -= capacity[idx]
            idx += 1
        
        return idx
            

