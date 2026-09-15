class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        table = [0 for _ in range(len(s) + 1)]
        for end in range(k, len(s) + 1):
            start = end - k
            table[end] = table[end - 1]
            if self.isPalindrome(s[start: end]):
                prev = 0 if start == 0 else table[start]
                table[end] = max(table[end], prev + 1)

            
            start = end - k - 1
            if start < 0:
                continue
            if self.isPalindrome(s[start: end]):
                prev = 0 if start == 0 else table[start]
                table[end] = max(table[end], prev + 1)
                
        return table[-1]

    def isPalindrome(self, substring):
        start = 0
        end = len(substring) - 1
        while start < end:
            if substring[start] == substring[end]:
                start += 1
                end -= 1
                continue
            
            return False
        
        return True