class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = {}
        for char in word:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
        
        order = sorted(counter.items(), reverse=True)
        result = 0
        num = 2
        batch = 1
        for _, count in order:
            result += batch * count
            num += 1
            if num > 9:
                num = 2
                batch += 1
        
        return result
