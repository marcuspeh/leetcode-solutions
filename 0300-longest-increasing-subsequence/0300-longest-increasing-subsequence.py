class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if not arr or arr[-1] < num:
                arr.append(num)
                continue
            
            start = 0
            end = len(arr) - 1
            
            while start < end:
                mid = start + (end - start) // 2
                if arr[mid] < num:
                    start = mid + 1
                else:
                    end = mid
            arr[start] = num
            
        return len(arr)