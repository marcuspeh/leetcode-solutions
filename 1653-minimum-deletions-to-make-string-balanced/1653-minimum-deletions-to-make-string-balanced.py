class Solution:
    def minimumDeletions(self, s: str) -> int:
        countA = []
        countB = []
        for i in range(len(s)):
            currA = 0
            if s[i] == 'a':
                currA += 1
            if i > 0:
                currA += countA[-1]
            countA.append(currA)

            currB = 0
            if s[len(s) - i - 1] == 'b':
                currB += 1
            if i > 0:
                currB += countB[-1]
            countB.append(currB)

        result = len(s)
        for i in range(len(s)):
            total = countA[i] + countB[len(s) - i - 1]
            result = min(result, len(s) - total)
        
        return result