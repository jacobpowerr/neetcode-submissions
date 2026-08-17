class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1

        for c in t:
            if c not in hashmap:
                return False
            else:
                hashmap[c] -= 1

        for val in hashmap.values():
            if val != 0:
                return False
        
        return True