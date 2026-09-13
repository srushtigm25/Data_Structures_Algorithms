class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = arr.copy()

        for i in range(len(arr)-1):
            maxv = arr[i+1]
            for j in range(i+1, len(arr)):
                maxv = max(maxv, arr[j])
            res[i] = maxv

        res[-1] = -1

        return res

