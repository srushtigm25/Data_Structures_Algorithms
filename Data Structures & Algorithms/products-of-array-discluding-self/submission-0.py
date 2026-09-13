class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n
        # res[0] = 1

        # for i in range(1,n):
        #     res[i] = res[i-1] * nums[i-1]

        # #res = [1,1,2,8]
        # #nums = [1,2,4,6]

        # R = 1
        # #[,12,8]
        # for i in range(n-1, -1, -1):
        #     res[i] = res[i] * R
        #     R = R * nums[i]
        # return res

        p = [1]
        pv = 1

        for n in nums:
            pv*=n
            p.append(pv)
        
        #[1,1,2,8,48]

        s = []
        sv =1

        for i in range(len(nums)-1, -1, -1):
            s.append(sv)
            sv *= nums[i]

        s.reverse()

        res = []
        for i in range(len(nums)):
            res.append(p[i] * s[i])
        return res
