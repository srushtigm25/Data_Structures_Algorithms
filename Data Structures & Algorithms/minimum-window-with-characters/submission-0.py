class Solution:
    def minWindow(self, s: str, t: str) -> str:
 
        if not t:
            return ""

        need = {}
        win = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        l = 0
        formed = 0
        required = len(need)
        min_len = float('inf')
        start = 0

        for r in range(len(s)):
            win[s[r]] = win.get(s[r], 0) + 1

            if s[r] in need and win[s[r]] == need[s[r]]:
                formed += 1

            while formed == required:
                win_len = r - l + 1

                if win_len < min_len:
                    min_len = win_len
                    start = l

                win[s[l]] -= 1

                if s[l] in need and win[s[l]] < need[s[l]]:
                    formed -= 1

                l += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]