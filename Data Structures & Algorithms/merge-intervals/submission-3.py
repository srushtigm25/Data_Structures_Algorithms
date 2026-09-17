class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # res = []

        # if len(intervals) == 0 or len(intervals) == 1:
        #     return intervals

        # for curr in range(1, len(intervals)):
        #     if intervals[curr][0] <= intervals[curr-1][1]:
        #         s = intervals[curr-1][0] 
        #         e = intervals[curr][1]
        #         res.append([s,e])
        #     else:
        #         # s = 
        #         res.append([intervals[curr][0], intervals[curr][1]])

        # return res
# Complexity:

# Sorting costs O(n log n).

# The traversal costs O(n).

# Total time is O(n log n).

# Result space can be O(n).


        #  Edge case
        if len(intervals) <= 1:
            return intervals

        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        # Put the first interval into result
        res = [intervals[0]]

        # Start from index 1 because index 0 is already in res
        for i in range(1, len(intervals)):

            curr = intervals[i]
            prev = res[-1]

            # Overlap
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])

            # No overlap
            else:
                res.append(curr)

        return res