class Solution:
    def sumGame(self, num: str) -> bool:
        firstHalf = 0
        secondHalf = 0
        firstHalfTurns = 0
        secondHalfTurns = 0
        n = len(num)
        for i in range(n):
            if num[i] == '?':
                if i < n / 2:
                    firstHalfTurns+= 1
                else:
                    secondHalfTurns += 1
            elif i < n / 2:
                firstHalf += int(num[i])
            else:
                secondHalf += int(num[i])
        if (firstHalfTurns + secondHalfTurns) % 2 == 1:
            return True
        
        if firstHalfTurns >= secondHalfTurns: 
            extraTurns = (firstHalfTurns - secondHalfTurns) / 2
            return firstHalf + secondHalfTurns * 9 + extraTurns * 9 != secondHalf + secondHalfTurns * 9
        else: 
            extraTurns = (secondHalfTurns - firstHalfTurns) / 2
            return firstHalf + firstHalfTurns * 9 != secondHalf + firstHalfTurns * 9 + extraTurns * 9


