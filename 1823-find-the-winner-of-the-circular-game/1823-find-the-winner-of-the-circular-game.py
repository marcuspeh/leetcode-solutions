class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = [i for i in range(1, n + 1)]
        index = 0
        
        while len(lst) > 1:
            index += k - 1
            index %= len(lst)
            
            lst.pop(index)
            
        return lst[0]