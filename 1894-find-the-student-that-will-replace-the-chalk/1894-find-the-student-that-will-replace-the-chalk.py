class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalFor1Round = sum(chalk)
        
        if totalFor1Round <= k:
            k = k % totalFor1Round
        
        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0:
                return i