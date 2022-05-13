class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        mini = min(arr)
        maxi = max(arr)
        gap = (maxi - mini) / (len(arr) - 1)
        
        if gap % 1:
            return False
        
        i = 0
        
        while i < len(arr):
            if mini + gap * i == arr[i]:
                i += 1
            else:
                index = (arr[i] - mini ) / gap
                
                if index % 1:
                    return False
                
                index = int(index)
                
                if arr[index] == arr[i]:
                    return False
                
                arr[i], arr[index] = arr[index], arr[i]
                
        return True
        