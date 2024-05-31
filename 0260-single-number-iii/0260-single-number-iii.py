class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        
        for num in nums:
            xor ^= num
        xor &= -xor
            
        result = [0, 0]
        for num in nums:
            if num & xor == 0:
                result[0] ^= num
            else:
                result[1] ^= num
        return result;