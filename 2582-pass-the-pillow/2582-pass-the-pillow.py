class Solution:
    def passThePillow(self, n, time):
        fullRounds = time // (n - 1)
        extraTime = time % (n - 1)

        if fullRounds % 2 == 0:
            return extraTime + 1 
        else:
            return n - extraTime 