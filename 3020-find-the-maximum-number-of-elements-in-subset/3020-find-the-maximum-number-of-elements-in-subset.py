class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
    
        result = 0
        if 1 in counter:
            result = counter[1]
            if result % 2 == 0:
                result -= 1
            counter.pop(1)

        for num in counter:
            curr = 0
            while num in counter and counter[num] > 1:
                curr += 2
                num *= num
            
            if num in counter:
                curr += 1
            else:
                curr -= 1
            
            result = max(result, curr)
    
        return result