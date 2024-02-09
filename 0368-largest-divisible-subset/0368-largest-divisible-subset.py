class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        table = [(num,) for num in nums]
        largest = (nums[0],)
        
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i - 1, -1, -1):
                if num < nums[j] or num % nums[j] != 0:
                    continue
                    
                temp = table[j] + (num,)
                if len(temp) < len(table[i]):
                    continue
                table[i] = temp
                if len(temp) > len(largest):
                    largest = table[i]
        return largest
            
            