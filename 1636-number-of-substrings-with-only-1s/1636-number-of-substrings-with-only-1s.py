class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        result = 0
        curr = 0
        for char in s:
            if char == '0':
                curr = 0
                continue
            
            curr += 1
            result += curr
            result %= MOD
        
        return result
