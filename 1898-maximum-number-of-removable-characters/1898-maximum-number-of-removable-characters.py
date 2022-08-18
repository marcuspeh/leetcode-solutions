class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left = 0
        right = len(removable)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if self.isStillSubString(s, p, removable, mid):
                left = mid + 1
            else:
                right = mid
        return left
            
    def isStillSubString(self, s, p, removable, k):
            i = 0
            j = 0
            remove = set(removable[:k + 1])
            while i < len(s) and j < len(p):
                if i in remove:
                    i += 1
                    continue
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            
            return j == len(p)