class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = str()
        for i in range(len(digits)):
            s += str(digits[i])
        sres = int(s) + 1

        result = [int(digit) for digit in str(sres)]

        return(result)