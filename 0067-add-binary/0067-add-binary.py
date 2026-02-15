class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        if len(a) < length:
            a = '0' * (length - len(a)) + a
        if len(b) < length:
            b = '0' * (length - len(b)) + b
        
        carry = 0
        result = []
        for i in range(length - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            result.append(str(carry % 2))
            carry //= 2
        
        if carry:
            result.append(str(carry))

        return "".join(result[::-1])