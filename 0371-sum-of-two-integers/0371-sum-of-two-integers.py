class Solution:
    def getSum(self, a: int, b: int) -> int:
        isBothNegative = a<0 and b<0
        mask = 0xffffffff
        add = a ^ b
        carry = (a & b) << 1
        
        while carry != 0:
            add, carry=(add ^ carry) & mask, ((add & carry) <<1) & mask
    
        return ~(add ^ mask) if isBothNegative else add