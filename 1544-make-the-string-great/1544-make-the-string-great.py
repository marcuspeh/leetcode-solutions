class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for char in s:
            if not result:
                result.append(char)
                continue
            if result[-1].lower() == char.lower() and result[-1] != char:
                result.pop()
                continue
            result.append(char)
        return "".join(result)