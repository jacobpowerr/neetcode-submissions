class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set()
        m_count = 0

        for n in nums:
            vals.add(n)

        for v in vals:
            if v - 1 not in vals:
                current = v
                length = 1
                while current + 1 in vals:
                    length += 1
                    current += 1
                m_count = max(length, m_count)

        return m_count