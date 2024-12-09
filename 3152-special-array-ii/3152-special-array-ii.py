class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        count = [0]
        for i in range(1, len(nums)):
            curr = count[-1]
            if nums[i] % 2 == nums[i - 1] % 2:
                curr += 1
            count.append(curr)
            
        result = []
        for start, end in queries:
            result.append(count[end] == count[start])
        return result