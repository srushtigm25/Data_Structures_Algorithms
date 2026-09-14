class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # n = len(nums)
        # i = 0

        # while i < n:
        #     if nums[i] == val:
        #         n -= 1
        #         nums[i]=nums[n]
        #     else:
        #         i+=1
        # return n


        k = 0

        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k
        
