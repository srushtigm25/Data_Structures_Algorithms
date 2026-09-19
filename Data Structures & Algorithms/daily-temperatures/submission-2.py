class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #This problem uses a monotonic stack and store indexes.
        res = [0] * len(temperatures)
        stack = []

        for curr_temp in range(len(temperatures)):

            while stack != [] and temperatures[curr_temp] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = curr_temp - prev_index
            stack.append(curr_temp)

        return res