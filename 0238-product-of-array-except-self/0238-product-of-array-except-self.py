class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]
        
        for num in nums[:-1]:
            arr.append(arr[-1] *  num)
            
        product = 1
        for i in range(len(nums) -1, -1, -1):
            arr[i] *= product
            product *= nums[i]
            
        return arr
            