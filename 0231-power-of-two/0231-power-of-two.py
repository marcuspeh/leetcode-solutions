class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        while n:
            count += n & 0x1
            n >>= 1

            if count > 1:
                break
        
        return count == 1