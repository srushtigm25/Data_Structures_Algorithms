class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        # for c in s:
        #     if c in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        
        # return True if not stack else False


        stack = []

        pairs = { ")" : "(", "]" : "[", "}" : "{" }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if stack == []:
                    return False
                if stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return stack == []