class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        
        def helper(index, lst, remainder):
            nonlocal result
            if remainder == 0:
                result.add(lst)
                
            if remainder < 0:
                return 
            if index >= len(candidates):
                return 
            
            currNumber = candidates[index]
            helper(index, lst + (currNumber,), remainder - currNumber)
            helper(index + 1, lst + (currNumber,), remainder - currNumber)
            helper(index + 1, lst, remainder)
            
        helper(0, tuple(), target)
        
        return list(result)
