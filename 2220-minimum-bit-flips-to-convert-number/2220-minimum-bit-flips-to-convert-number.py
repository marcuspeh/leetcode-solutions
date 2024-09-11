class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start == 0 and goal == 0:
            return 0

        flip = 1 if (start & 1) != (goal & 1) else 0
        return flip + self.minBitFlips(start >> 1, goal >> 1)