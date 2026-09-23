class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1
        length = 0

        while l < r:
            length = r - l
            area = max(area, length * (min(heights[l], heights[r])))

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return area