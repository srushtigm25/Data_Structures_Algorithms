class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # for i in range(len(nums)):
        #     while i + nums[i] <= len(nums)-1:
        #         i += nums[i]
        #     return True
        # return False

        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, i+nums[i])
        return True

            
#        Time: O(n)
# Space: O(1)