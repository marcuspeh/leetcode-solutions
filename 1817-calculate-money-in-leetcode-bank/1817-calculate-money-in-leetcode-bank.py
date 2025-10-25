class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 0
        prev = 0
        bank = 0
        for i in range(n):
            if i % 7 == 0:
                prev = monday 
                monday += 1

            prev += 1
            bank += prev
            
        return bank