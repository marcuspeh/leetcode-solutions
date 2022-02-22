class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        
        # Something like Base 26
        for title in columnTitle:
            result = result * 26 + self.convertToNumber(title)
            
        return result 

    # Convert to position
    def convertToNumber(self, letter):
        ordOfA = 65
        return ord(letter) - ordOfA + 1