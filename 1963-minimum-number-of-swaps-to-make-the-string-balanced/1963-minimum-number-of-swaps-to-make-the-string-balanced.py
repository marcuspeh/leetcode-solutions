class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        result = 0
        for char in s:
            if char == '[':
                stack.append(char)
                continue
            if stack:
                stack.pop()
                continue
            result += 1
        return (result + 1) // 2