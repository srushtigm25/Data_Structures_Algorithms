class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # n1 = len(s1)
        # n2 = len(s2)

        # if n1>n2:
        #     return False

        # counts1 = [0] * 26
        # counts2 = [0] * 26

        # for i in range(n1):
        #     counts1[ord(s1[i])- 97] +=1
        #     counts2[ord(s2[i]) - 97] +=1

        # if counts1 == counts2:
        #     return True

        # for i in range(n1,n2):
        #     counts2[ord(s2[i]) - 97] +=1
        #     counts2[ord(s2[i-n1]) - ord('a')] -=1

        #     if counts1 == counts2:
        #         return True

        # return False
        need = {}
        window = {}
        l1 = len(s1)
        l = 0

        for i in s1:
            need[i] = need.get(i, 0) + 1

        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1

            if r-l+1 > l1:
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l+=1
            
            if window == need:
                return True

        return False


