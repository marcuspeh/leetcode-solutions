class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        actualRotation = k % len(nums)
        
        if actualRotation > len(nums) // 2:
            self.moveBack(nums, actualRotation)
        else:
            self.moveFront(nums, actualRotation)
        
    def moveBack(self, nums, k):
        for _ in range(len(nums) - k):
            temp = nums.pop(0)
            nums.append(temp)
    
    def moveFront(self, nums, k):
        for _ in range(k):
            temp = nums.pop()
            nums.insert(0, temp)
            
        