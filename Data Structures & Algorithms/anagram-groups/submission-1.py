class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)

        # for s in strs:
        #     sorteds = "".join(sorted(s))
        #     res[sorteds].append(s)
        # return list(res.values())

        group = {}

        for s in strs:
            k = "".join(sorted(s))
            group.setdefault(k,[]).append(s)

        return list(group.values())
            
      



