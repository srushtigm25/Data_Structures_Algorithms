class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    if words[i] not in res:
                        res.append(words[i])

                elif words[j] in words[i]:
                    if words[j] not in res:
                        res.append(words[j])
        return res