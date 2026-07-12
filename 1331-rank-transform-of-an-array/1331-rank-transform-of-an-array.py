class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranking = list(sorted(set(arr)))
        rankMap = {}
        for i in range(len(ranking)):
            rankMap[ranking[i]] = i + 1
        
        for i in range(len(arr)):
            num = arr[i]
            arr[i] = rankMap[num]
        
        return arr