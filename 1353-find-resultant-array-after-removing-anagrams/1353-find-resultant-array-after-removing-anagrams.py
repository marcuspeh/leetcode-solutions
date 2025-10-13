class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prevCount = []

        for word in words:
            count = sorted(word)
            print(count)
            if prevCount == count:
                continue

            prevCount = count
            result.append(word)
        
        return result
            