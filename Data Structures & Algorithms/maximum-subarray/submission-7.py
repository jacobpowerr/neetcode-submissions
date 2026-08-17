class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        running_sum = 0

        for num in nums:
            running_sum += num
            maxSub = max(maxSub, running_sum)
            if running_sum < 0:
                running_sum = 0

        return maxSub