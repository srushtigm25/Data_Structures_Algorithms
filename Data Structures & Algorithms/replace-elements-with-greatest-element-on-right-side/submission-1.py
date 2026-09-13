class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # res = arr.copy()

        # for i in range(len(arr)-1):
        #     maxv = arr[i+1]
        #     for j in range(i+1, len(arr)):
        #         maxv = max(maxv, arr[j])
        #     res[i] = maxv

        # res[-1] = -1

        # return res

        # Time: O(n²)
        # Space: O(n)

        max_r = -1

        for i in range(len(arr)-1, -1 , -1):
            curr = arr[i]
            arr[i] = max_r
            max_r = max(max_r, curr)
        return arr

