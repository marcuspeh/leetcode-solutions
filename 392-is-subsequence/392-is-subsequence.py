class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerS = 0
        pointerT = 0
        
        while pointerT < len(t) and pointerS < len(s):
            if s[pointerS] == t[pointerT]:
                pointerS += 1
            pointerT += 1
        
        return pointerS == len(s)