class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}

        for c in s:
            if c not in hashmap_s:
                hashmap_s[c] = 1
            else:
                hashmap_s[c] += 1

        for c in t:
            if c not in hashmap_t:
                hashmap_t[c] = 1
            else:
                hashmap_t[c] += 1

        if hashmap_t == hashmap_s:
            return True
        
        return False