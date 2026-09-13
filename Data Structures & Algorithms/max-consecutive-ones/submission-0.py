class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_streak = 0
        maxc = 0
        for i in nums:
            if i == 1:
                curr_streak +=1
            else:
                curr_streak = 0

            maxc = max(maxc, curr_streak)
            
        return maxc
#         Time: O(n)
# Space: O(1)