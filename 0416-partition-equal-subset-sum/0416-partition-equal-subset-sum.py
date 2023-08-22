class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        table = [False for _ in range(target + 1)]
        table[0] = True
        
        for num in nums:
            for n in range(target, 0, -1):
                if n - num < 0:
                    continue
                table[n] = table[n] or table[n - num]

        return table[target]