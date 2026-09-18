class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # intervals.sort(key = lambda x: x[0])
        # res = 0

        # for i in range(1, len(intervals)):
        #     cs = intervals[i][0]
        #     ce = intervals[i][1]

        #     ps = intervals[i-1][0]
        #     pe = intervals[i-1][1]

        #     if cs < pe:
        #         rem_elem = max(ce, pe)
        #         intervals.remove(intervals[i])
        #         res +=1

        # return res

        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[0])

        res = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            cs = intervals[i][0]
            ce = intervals[i][1]

            if cs < end:
                res += 1
                end = min(end, ce)
            else:
                end = ce

        return res