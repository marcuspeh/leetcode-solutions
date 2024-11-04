class Solution:
    def compressedString(self, word: str) -> str:
        result = []
        count = 0
        prev = None
        
        for character in word:
            if character != prev:
                self.add(result, count, prev)
                prev = character
                count = 0
            count += 1
        
        self.add(result, count, prev)
        return "".join(result)
    
    def add(self, result, count, char):
        if char == None:
            return
                
        while count > 0:
            result.append(str(min(9, count)))
            result.append(char)
            count -= 9
        
        