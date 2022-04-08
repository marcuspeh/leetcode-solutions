class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def helper(lst, combi):
            nonlocal result
            if len(combi) == k:
                result.append(combi)
                return
            
            if not lst:
                return
            
            for i in range(len(lst)):
                helper(lst[i + 1:], combi + [lst[i]])
            
        helper(list(range(1, n + 1)), [])
        
        return result