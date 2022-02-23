class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        highest = nums[0]
        currN = nums[0]
        curr = nums[0]
        
        for n in nums[1:]:
            if n < 0:
                temp = currN
                currN = curr
                curr = temp
            
            curr = max(curr * n, n)
            currN = min(currN * n, n)
            
            highest = max(highest, curr)
            
        return highest