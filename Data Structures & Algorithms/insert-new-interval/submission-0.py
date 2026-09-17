class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []


        if len(intervals) == 0:
            return [newInterval]

        if len(intervals) >= 1:
            for i in range(len(intervals)):
                s, e = intervals[i]
                if e < newInterval[0]:
                    res.append([s, e])
                elif newInterval[1] < s:
                    res.append(newInterval)
                    return res + intervals[i:]
                else:
                    newInterval[0] = min(s, newInterval[0])
                    newInterval[1] = max(e, newInterval[1])

            res.append(newInterval)

        return res