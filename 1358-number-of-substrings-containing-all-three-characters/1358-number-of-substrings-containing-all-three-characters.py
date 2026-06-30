class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {}
        start = 0
        end = 0
        result = 0
        while end < len(s):
            char = s[end]
            if char not in count:
                count[char] = 0
            count[char] += 1

            firstChar = s[start]
            while len(count) == 3 and count[firstChar] >= 1:
                count[firstChar] -= 1
                if count[firstChar] == 0:
                    del count[firstChar]

                start += 1
                result += len(s) - end
                firstChar = s[start]

            end += 1
        
        return result



