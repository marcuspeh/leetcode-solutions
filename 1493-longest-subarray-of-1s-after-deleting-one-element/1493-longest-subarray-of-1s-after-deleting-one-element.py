class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cumulate = []
        curr = 0
        for num in nums:
            if num == 0:
                if curr:
                    cumulate.append(curr)
                cumulate.append(0)
                curr = 0
                continue
            
            curr += 1
        
        cumulate.append(curr)
        print(cumulate)

        result = 0
        for i in range(len(cumulate)):
            if i == 0:
                result = max(result, cumulate[i] - 1)
                continue
            
            if i == 1:
                result = max(result, cumulate[i])
                continue

            result = max(result, cumulate[i] + cumulate[i - 2])
        
        return result
