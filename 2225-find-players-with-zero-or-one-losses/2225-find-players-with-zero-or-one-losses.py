class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matchCount = {}
        lostMoreThanOne = set()
        
        for winner, loser in matches:
            if winner not in lostMoreThanOne and winner not in matchCount:
                matchCount[winner] = 0
            
            if loser in lostMoreThanOne:
                continue
                
            if loser not in matchCount:
                matchCount[loser] = 0
            matchCount[loser] += 1
            
            if matchCount[loser] > 1:
                matchCount.pop(loser)
                lostMoreThanOne.add(loser)
        
        nvrLost = []
        lostOnce = []
        
        for player, count in matchCount.items():
            if count:
                lostOnce.append(player)
                continue
            nvrLost.append(player)
        return sorted(nvrLost), sorted(lostOnce)