class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def helper(isAliceTurn, i, m):
            if i >= len(piles):
                return 0, 0
            
            resultScoreAlice = 0
            resultScoreBob = 0
            scoreAlice = 0
            scoreBob = 0
            for j in range(1, m * 2 + 1):
                currIdx = i + j
                if currIdx >= len(piles):
                    break
                    
                if isAliceTurn:
                    scoreAlice += piles[currIdx]
                else:
                    scoreBob += piles[currIdx]
                
                currAlice, currBob = helper(not isAliceTurn, currIdx, max(m, j))
                currAlice += scoreAlice
                currBob += scoreBob
                if isAliceTurn and currAlice > resultScoreAlice:
                    resultScoreAlice = currAlice
                    resultScoreBob = currBob
                elif not isAliceTurn and currBob > resultScoreBob:
                    resultScoreAlice = currAlice
                    resultScoreBob = currBob
            return resultScoreAlice, resultScoreBob
            
        return helper(True, -1, 1)[0]