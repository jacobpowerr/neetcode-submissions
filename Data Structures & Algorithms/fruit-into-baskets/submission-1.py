class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_s = 0
        l = 0
        count = {}

        for r in range(len(fruits)):
            if fruits[r] not in count:
                count[fruits[r]] = 1
            else:
                count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            max_s = max(r - l + 1, max_s)

        return max_s