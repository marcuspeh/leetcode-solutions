class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = (end - start) // 2 + start
            
            if mid != 0 and mid != len(arr) - 1:
                if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                    return mid
                elif arr[mid - 1] > arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif mid == 0:
                if arr[mid] > arr[mid + 1]:
                    return mid
                else:
                    start = mid + 1
            else:
                if arr[mid] > arr[mid - 1]:
                    return mid
                else:
                    end = mid - 1
        return -1