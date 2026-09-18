class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm.

        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            start_fresh = nums[i]
            continue_ = curr_sum + nums[i]

            if start_fresh > continue_:
                curr_sum = start_fresh
            else:
                curr_sum = continue_

            max_sum = max(max_sum, curr_sum)


        return max_sum

# Time: O(n)
# Space: O(1)