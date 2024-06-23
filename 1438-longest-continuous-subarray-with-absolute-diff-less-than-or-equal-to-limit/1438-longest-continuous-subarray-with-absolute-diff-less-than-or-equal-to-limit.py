class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()
        minDeque = deque()
        left = 0
        maxLength = 0

        for right in range(len(nums)):
            while maxDeque and maxDeque[-1] < nums[right]:
                maxDeque.pop()
            maxDeque.append(nums[right])

            while minDeque and minDeque[-1] > nums[right]:
                minDeque.pop()
            minDeque.append(nums[right])

            while maxDeque[0] - minDeque[0] > limit:
                if maxDeque[0] == nums[left]:
                    maxDeque.popleft()
                if minDeque[0] == nums[left]:
                    minDeque.popleft()
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength