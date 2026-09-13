class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r= len(heights)-1
        maxa = 0

        while l<r:
            hi = min(heights[l], heights[r])
            wi = r-l
            maxa = max(maxa, (hi * wi))
            if heights[l]<= heights[r]:
                l+=1
            else:
                r-=1
        return maxa



   
            
