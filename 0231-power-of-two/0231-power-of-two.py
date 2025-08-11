class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        while n > 0:
            count += n & 0x1
            n = n >> 1
        return count == 1