class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #amount = 0, return 0
        #amount < sum(coins), check the dp and return fewest number of coins to make up exact target amount
        # 1 * 12 = 12 coins
        # 5 * 2 + 1 * 2 = 4 coins
        # 10 * 1 + 1* 2 = 3 coins , return min(12,4,3)
        # need 2D DP bcoz of 2 elements add upto target 
#         Now define the DP state.
# dp[a] = minimum number of coins needed to make amount a
# Only ONE thing describes our state, the amount.
# So this is 1D DP.


        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for a in range(1, amount+1):

            for coin in coins:

                if coin <= a:

                    dp[a] = min(dp[a], 1+dp[a - coin])

        if dp[amount] == float('inf'):
            return -1

        return dp[amount]