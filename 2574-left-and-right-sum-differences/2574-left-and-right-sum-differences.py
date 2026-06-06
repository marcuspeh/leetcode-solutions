class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        leftSum = 0
        answer = []
        for n in nums:
            rightSum = total - n - leftSum
            answer.append(abs(leftSum - rightSum))
            leftSum += n
        return answer