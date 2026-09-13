class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest = 0
        # l = 0
        # counts = [0]*26

        # for r in range(len(s)):
        #     counts[ord(s[r])-ord('A')] += 1
        #     while (r-l+1) - max(counts) >k:
        #         counts[ord(s[l])-ord('A')] -=1
        #         l+=1
        #     longest = max(longest, r-l+1)
        # return longest

        l = 0
        freq = {}
        maxf = 0
        maxl = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            maxf = max(maxf, freq[s[r]])

            while (r-l+1) - maxf > k:
                freq[s[l]] -= 1
                l += 1

            maxl = max(maxl,r-l+1 )
        return maxl