class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNumber = float("inf")
        secondNumber = float("inf")
        
        for n in nums:
            if n <= firstNumber:
                firstNumber = n
            elif n <= secondNumber:
                secondNumber = n
            else:
                return True
        
        return False