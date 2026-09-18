class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            count += n & 1
            n >>= 1

        return count

#         Time: O(log n), at most 32 iterations because n is 32-bit.
# Space: O(1).