class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0

        for i, n in enumerate(nums):
            if n != 0:
                nums[k] = n
                k+=1
        
        for i in range(k,len(nums)):
            nums[i] = 0

        