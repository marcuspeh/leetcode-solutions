class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        biggest = 0
        secondBiggest = 0
        smallest = inf
        secondSmallest = inf
        
        for num in nums:
            if num > biggest:
                secondBiggest = biggest
                biggest = num
            else:
                secondBiggest = max(secondBiggest, num)
                
            if num < smallest:
                secondSmallest = smallest
                smallest = num
            else:
                secondSmallest = min(secondSmallest, num)
        
        return biggest * secondBiggest - smallest * secondSmallest