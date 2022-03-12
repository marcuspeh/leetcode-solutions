class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = ""
        
        zero = ord('0')
        
        pointer1 = len(num1) - 1
        pointer2 = len(num2) - 1
        
        while pointer1 >= 0 and pointer2 >= 0:
            a = ord(num1[pointer1]) - zero
            b = ord(num2[pointer2]) - zero
        
            total = a + b + carry
            
            if total >= 10:
                carry = 1
                total %= 10
            else:
                carry = 0
            
            result = chr(zero + total) + result
            pointer1 -= 1
            pointer2 -= 1
        
        
        
        while pointer1 >= 0:
            if not carry:
                result = num1[0:pointer1 + 1] + result
                break
                
            a = ord(num1[pointer1]) - zero
        
            total = a + carry
            
            if total >= 10:
                carry = 1
                total %= 10
            else:
                carry = 0
            
            result = chr(zero + total) + result
            pointer1 -= 1
        
        while pointer2 >= 0:
            if not carry:
                result = num2[0:pointer2 + 1] + result
                break
                
            a = ord(num2[pointer2]) - zero
        
            total = a + carry
            
            if total >= 10:
                carry = 1
                total %= 10
            else:
                carry = 0
            
            result = chr(zero + total) + result
            pointer2 -= 1
        if carry:
            return "1" + result
        
        return result
            