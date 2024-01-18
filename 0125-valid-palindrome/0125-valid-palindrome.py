class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        self.start = 0
        self.end = len(s) - 1
        
        while self.start < self.end:
            front = self.getNext(s)
            back = self.getPrev(s)
            
            if front and back and front != back:
                return False
        
        return True
        
    def getNext(self, s):
        while self.start < len(s) and not s[self.start].isalnum():
            self.start += 1
        self.start += 1
        if self.start > len(s):
            return ''
        
        return s[self.start - 1]
    
    def getPrev(self, s):
        while self.end >= 0 and not s[self.end].isalnum():
            self.end -= 1
        self.end -= 1
        if self.end < 0:
            return ''
        
        return s[self.end + 1]