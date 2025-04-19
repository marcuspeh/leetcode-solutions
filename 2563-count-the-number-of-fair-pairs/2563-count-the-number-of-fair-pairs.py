class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.count(nums, upper + 1) - self.count(nums, lower)

    def count(self, arr, limit):
        result = 0
        i = 0
        j = len(arr) - 1

        while i < j:
            total = arr[i] + arr[j]
            if total < limit:
                result += j - i
                i += 1
                continue
            j -= 1
        
        return result