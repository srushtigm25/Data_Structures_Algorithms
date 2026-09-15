class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # s = str()
        # for i in range(len(digits)):
        #     s += str(digits[i])
        # sres = int(s) + 1

        # result = [int(digit) for digit in str(sres)]

        # return(result)

#         Time complexity: O(n)
# Space complexity: O(n)


        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1]+digits

