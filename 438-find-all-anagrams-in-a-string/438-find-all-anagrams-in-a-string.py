class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        lengthP = len(p)
        
        # Set up counter to compare
        counter = {}
        for i in p:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        # Sliding window
        for i in range(len(p)):
            if s[i] in counter:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
            else:
                counter[s[i]] = -1
                
        result = []
        
        if len(counter) == 0:
            result.append(0)
        
        for i in range(len(s) - lengthP):
            print(counter)
            # get rid of letter at left pointer
            if s[i] in counter:
                counter[s[i]] += 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
            else:
                counter[s[i]] = 1
            
            # Take into acc right pointer
            if s[i + lengthP] in counter:
                counter[s[i + lengthP]] -= 1
                if counter[s[i + lengthP]] == 0:
                    del counter[s[i + lengthP]]
            else:
                counter[s[i + lengthP]] = -1
                
            # Check if anagram in new dictionary
            if len(counter) == 0:
                result.append(i + 1)
                
        return result
            
            
                
                
        