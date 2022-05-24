class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        
        result = 0
        
        for n in arr1:
            if self.checkArr(n, arr2, d):
                result += 1
        
        return result

    def checkArr(self, n, arr2, d):
        start = 0
        end = len(arr2) - 1
        
        while start <= end:
            mid = (end - start) // 2 + start
            
            if abs(arr2[mid] - n) <= d:
                return False
            elif arr2[mid] > n:
                end = mid - 1
            else:
                start = mid + 1
        
        return True