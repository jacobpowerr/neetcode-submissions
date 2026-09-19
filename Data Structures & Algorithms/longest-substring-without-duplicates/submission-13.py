class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_s = 0
        l = 0
        r = 1
        if not s:
            return 0
        visit = set(s[l])

        if len(s) == 1:
            return 1

        while r < len(s):
            if s[r] not in visit:
                visit.add(s[r])
                r += 1
            else:
                while s[r] in visit:
                    visit.remove(s[l])
                    l += 1
            max_s = max(max_s, r - l)

        return max_s