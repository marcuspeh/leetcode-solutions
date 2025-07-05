class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        for num in arr:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        result = -1
        for num, cnt in count.items():
            if num != cnt:
                continue
            
            result = max(result, num)
        return result