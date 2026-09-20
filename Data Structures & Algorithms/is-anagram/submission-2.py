class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        if len(t) != len(s):
            return False

        for c in t:
            if c in count_t:
                count_t[c] += 1
            else:
                count_t[c] = 1

        for c in s:
            if c in count_s:
                count_s[c] += 1
            else:
                count_s[c] = 1

        if count_t == count_s:
            return True

        return False