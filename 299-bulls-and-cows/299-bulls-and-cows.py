class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        
        cache = {}
        possibleCow = []
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] not in cache:
                    cache[secret[i]] = 0
                cache[secret[i]] += 1
                possibleCow.append(guess[i])
                
        for i in possibleCow:
            if i in cache and cache[i] > 0:
                cow += 1
                cache[i] -= 1
                
        return f"{bull}A{cow}B"