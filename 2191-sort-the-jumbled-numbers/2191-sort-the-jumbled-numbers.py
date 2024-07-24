class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: self.getMappedNum(x, mapping))
        return nums
        
    def getMappedNum(self, num, mapping):               
        result = 0
        for n in str(num):
            result = result * 10 + mapping[int(n)]
        return result
