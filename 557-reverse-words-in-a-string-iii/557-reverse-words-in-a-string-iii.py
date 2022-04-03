class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        for i in range(len(lst)):
            lst[i] = self.reverseWord(lst[i])
        return " ".join(lst)
    
    def reverseWord(self, s):
        result = ""
        for i in range(len(s) - 1, -1, -1):
            result += s[i]
        return result