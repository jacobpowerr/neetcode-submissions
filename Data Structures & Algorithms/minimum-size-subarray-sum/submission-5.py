class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = len(nums)
        curr = 0
        l = 0

        for r in range(len(nums)):
            curr = curr + nums[r]
            if curr >= target:
                while curr >= target:
                    curr -= nums[l]
                    l += 1
                shortest = min(shortest, r - l + 2)

        nums = sum(nums)

        if nums < target:
            return 0

        return shortest