class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sr = 0 
        sl = sum(nums)
        for i in range(0, len(nums)+1):
            sr += i
        return sr-sl
            