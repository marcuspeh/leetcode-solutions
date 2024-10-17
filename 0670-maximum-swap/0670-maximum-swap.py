class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        
        postmax = [(num[-1], len(num) - 1) for _ in num]
        for i in range(len(num) - 2, -1, -1):
            curr = (num[i], i)
            
            if curr[0] <= postmax[i + 1][0]:
                curr = postmax[i + 1]
            postmax[i] = curr
            
        for i in range(len(num) - 1):
            if postmax[i + 1][0] <= num[i]:
                continue
            
            idx = postmax[i + 1][1]
            num[i], num[idx] = num[idx], num[i]
            break
        
        return int("".join(num))