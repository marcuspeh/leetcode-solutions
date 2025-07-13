class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        playerIdx = 0
        trainerIdx = 0
        result = 0
        while playerIdx < len(players) and trainerIdx < len(trainers):
            if players[playerIdx] <= trainers[trainerIdx]:
                result += 1
                playerIdx += 1
                trainerIdx += 1
                continue
            
            trainerIdx += 1
    
        return result