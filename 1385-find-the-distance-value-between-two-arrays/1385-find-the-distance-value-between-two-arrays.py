class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        
        for i in range(len(arr1)):
            add = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    add = False
                    break
            if add:
                result += 1
        
        return result
        
        