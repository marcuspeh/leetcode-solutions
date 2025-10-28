class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prevCount = self.countDevice(bank[0])
        for i in range(1, len(bank)):
            currCount = self.countDevice(bank[i])
            if currCount == 0:
                continue
                
            result += prevCount * currCount
            prevCount = currCount
        
        return result


    def countDevice(self, row):
        return row.count("1")