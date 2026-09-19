class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     sum = 0 
        #     for j in range(i,len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             res += 1
        # return res

        # res = 0
        # curs = 0
        # seen = defaultdict(int)
        # seen[0] = 1

        # for n in nums:
        #     curs += n
        #     res += seen[curs- k]
        #     seen[curs] += 1
        # return res

        prefix_sum = {0:1}
        count = 0
        curr_sum = 0

        for n in nums:
            curr_sum += n
            count += prefix_sum.get(curr_sum - k, 0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        return count

        

