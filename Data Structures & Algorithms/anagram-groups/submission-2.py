class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}
        d2 = {}
        for st in strs:
            d1[st] = tuple(sorted(st))
        for st in strs:
            if d1[st] in d2:
                d2[d1[st]].append(st)
            else:
                d2[d1[st]] = [st]
        return list(d2.values())
        

        



