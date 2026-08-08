class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        twice = {}

        for num in nums:
            if num in twice:
                twice[num] += 1
                if twice[num] == 2:
                    return True
            else:
                twice[num] = 1
        
        return False