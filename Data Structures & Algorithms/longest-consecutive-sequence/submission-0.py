class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store = set(nums)
        # res = 0 

        # for n in nums:
        #     streak , cur = 0, n
        #     while cur in store:
        #         streak += 1
        #         cur += 1
        #     res = max(res, streak)
        # return res
        numset = set(nums)
        longest = 0 

        for n in numset:
            if (n-1) not in numset:
                length = 1
                while(n + length) in numset:
                    length += 1
                longest = max(length, longest)
        return longest
            




        