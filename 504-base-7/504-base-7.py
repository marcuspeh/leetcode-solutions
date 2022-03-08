class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        result = ""
        isNegative = num < 0
        
        if isNegative:
            num = -num
        
        while num:
            toInsert = num % 7
            num = num // 7
            result = f"{toInsert}{result}"
        
        if isNegative:
            return "-" + result
        else:
            return result