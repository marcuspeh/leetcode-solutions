class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0, len(s), k):
            curr = s[i: i + k]
            if i + k > len(s):
                curr += fill * (i + k - len(s))
            result.append(curr)
        
        return result