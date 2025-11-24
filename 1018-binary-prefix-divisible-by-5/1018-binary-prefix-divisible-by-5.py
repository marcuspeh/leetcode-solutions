class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = 0
        result = []
        for num in nums:
            curr = curr << 1 | num
            result.append(curr % 5 == 0)
        
        return result