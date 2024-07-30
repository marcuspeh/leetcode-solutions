class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        aCount = sum(1 for ch in s if ch == "a")

        bCount = 0
        minDeletions = n

        for ch in s:
            if ch == "a":
                aCount -= 1
            minDeletions = min(minDeletions, aCount + bCount)
            if ch == "b":
                bCount += 1

        return minDeletions