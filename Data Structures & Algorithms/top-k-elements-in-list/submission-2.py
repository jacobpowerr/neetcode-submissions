class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for i, n in count.items():
            freq[n].append(i)

        for i in range(len(freq) - 1, -1, -1):
            if len(res) == k:
                return res
            if freq[i] == []:
                continue
            for num in freq[i]:
                res.append(num)