class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        hasCarry = True
        idx = len(digits) - 1
        while hasCarry and idx >= 0:
            digits[idx] += 1
            hasCarry = digits[idx] > 9
            digits[idx] = digits[idx] % 10
            idx -= 1
        
        if hasCarry:
            temp = [1]
            temp.extend(digits)
            digits = temp
        
        return digits