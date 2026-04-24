class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        location = 0
        wildcard = 0
        for move in moves:
            if move == "L":
                location -= 1
                continue
            
            if move == "R":
                location += 1
                continue
            
            wildcard += 1
        
        return abs(location) + wildcard