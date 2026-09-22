class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = len(nums) + 1
        l = 0
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                curr -= nums[l]
                shortest = min(shortest, r - l + 1)
                l += 1

        return 0 if shortest == len(nums) + 1 else shortest