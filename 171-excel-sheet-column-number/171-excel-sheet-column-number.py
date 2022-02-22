class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        base = 1
        
        # Something like Base 26
        for i in range(len(columnTitle) - 1, -1, -1):
            title = columnTitle[i]
            result += self.convertToNumber(title) * base
            base *= 26
            
        return result 

    # Convert to position
    def convertToNumber(self, letter):
        ordOfA = 65
        return ord(letter) - ordOfA + 1