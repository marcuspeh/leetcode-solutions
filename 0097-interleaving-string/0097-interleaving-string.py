class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [True for _ in range(len(s2) + 1)] 
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            
            for j in range(1, len(s2) + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i - 1 + j]) or (dp[j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[-1]