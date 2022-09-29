class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        
        for i in range(len(text2)):
            for j in range(len(text1)):
                tableI = i + 1
                tableJ = j + 1
                
                if text1[j] == text2[i]:
                    table[tableI][tableJ] = table[i][j] + 1
                else:
                    table[tableI][tableJ] = max(table[tableI][j], table[i][tableJ])
        
        return table[-1][-1]