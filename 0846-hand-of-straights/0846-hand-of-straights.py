class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        groups = []
        hand.sort()
        
        for card in hand:                
            isInserted = False
            
            for group in groups:
                if len(group) == groupSize:
                    continue
                    
                if group[-1] == card:
                    continue
                
                if group[-1] != card - 1:
                    return False
                
                group.append(card)
                isInserted = True
                break
            
            if not isInserted:
                groups.append([card])
        
        for group in groups:
            if len(group) != groupSize:
                return False
        return True