class Solution:
    def minimumDeletions(self, s: str) -> int:
        prefixB = []
        for char in s:
            if not prefixB:
                curr = 0
            else:
                curr = prefixB[-1]
            if char == "b":
                curr += 1
            prefixB.append(curr)
        
        postfixA = []
        for i in range(len(s) - 1, -1, -1):
            if not postfixA:
                curr = 0
            else:
                curr = postfixA[-1]
            if s[i] == "a":
                curr += 1
            postfixA.append(curr)
        postfixA = postfixA[::-1]
        
        result = min(prefixB[-1], postfixA[0])
        for i in range(1, len(s) - 1):
            result = min(result, postfixA[i] + prefixB[i + 1], postfixA[i] + prefixB[i - 1])
        return result
            