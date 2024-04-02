class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        checked = set()
        mapping = {}

        for i in range(len(s)):
            word = s[i]
            if word in mapping:
                word = mapping[word]
                if t[i] != word:
                    return False
            else:
                if t[i] in checked:
                    return False
                mapping[word] = t[i]
            checked.add(t[i])
                
        return True