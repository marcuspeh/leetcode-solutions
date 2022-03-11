class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNumber = secondNumber = 1 << 32
        
        for n in nums:
            if n <= firstNumber:
                firstNumber = n
            elif n <= secondNumber:
                secondNumber = n
            else:
                return True
        
        return False