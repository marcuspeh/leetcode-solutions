class Solution:
    def minimumSteps(self, s: str) -> int:
        total = 0
        curr = 0
        for i in range(len(s) - 1, -1, -1):
            prev = curr
            if s[i] == "0":
                curr += 1
                continue
            total += prev
        return total