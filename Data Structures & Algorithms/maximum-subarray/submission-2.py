class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        runSum = 0

        for n in nums:
            runSum = runSum + n
            maxSub = max(maxSub, runSum)
            if runSum < 0:
                runSum = 0

        return maxSub