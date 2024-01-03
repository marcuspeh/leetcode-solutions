class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev = 0
        
        for row in bank:
            curr = sum(int(val) for val in row)
            if curr == 0:
                continue
            result += self.combination(prev, curr)
            prev = curr
        
        return result
        
    def combination(self, row1, row2):
        return row1 * row2