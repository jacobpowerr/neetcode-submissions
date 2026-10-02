class Solution:
    def isValid(self, s: str) -> bool:
        p = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c not in p:
                stack.append(c)
            elif stack and p[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack