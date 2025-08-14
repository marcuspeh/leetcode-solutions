class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = ""
        prev = ""
        count = 0
        for char in num:
            if char != prev:
                prev = char
                count = 0
            
            count += 1
            if count == 3:
                result = max(result, char)
        
        return result * 3