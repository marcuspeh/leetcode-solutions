class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def helper(lst, total):
            nonlocal result
            
            if total == n:
                if len(lst) == k:
                    result.append(lst)
                return
            elif total > n:
                return
            
            if lst:
                prev = lst[-1]
            else:
                prev = 0
            
            for i in range(prev + 1, 10):
                helper(lst + [i], total + i)
                
        helper([], 0)
        
        return result