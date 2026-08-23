class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = {}

        for i in range(len(strs)):
            sorted_s = ''.join(sorted(strs[i]))
            if sorted_s in hashmap:
                hashmap[sorted_s].append(strs[i])
            else:
                hashmap[sorted_s] = [strs[i]]

        for lists in hashmap.values():
            res.append(lists)


        return res