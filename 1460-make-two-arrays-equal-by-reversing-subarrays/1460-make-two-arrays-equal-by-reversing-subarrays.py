class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = {}
        for character in target:
            if character not in counter:
                counter[character] = 0
            counter[character] += 1
        
        for character in arr:
            if character not in counter or counter[character] <= 0:
                return False
            
            counter[character] -= 1
        
        return True