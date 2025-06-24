class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []
        prev = 0
        i = 0
        while i < len(nums):
            if nums[i] == key:
                start = max(prev, i - k)
                end = min(i + k + 1, len(nums))
                for idx in range(start, end):
                    result.append(idx)
                
                prev = end
            i+= 1
        
        return result

