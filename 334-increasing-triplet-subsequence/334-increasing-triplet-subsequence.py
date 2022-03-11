class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNumber = 1 << 32
        secondNumber = 1 << 32
        
        for n in nums:
            if n <= firstNumber:
                firstNumber = n
            elif n <= secondNumber:
                secondNumber = n
            else:
                return True
        
        return False