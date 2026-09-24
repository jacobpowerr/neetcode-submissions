class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums) / 2
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
            if count[n] > half:
                return n