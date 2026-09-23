class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for r in range(n):
            while stack and stack[-1][0] < temperatures[r]:
                temp, i = stack.pop()
                res[i] = r - i

            stack.append((temperatures[r], r))

        return res