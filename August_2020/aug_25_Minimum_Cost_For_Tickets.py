class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        days = set(days)

        for i in range(1, last_day + 1):
            if i in days:
                one = costs[0] + dp[i - 1]
                seven = costs[1] + dp[max(i - 7, 0)]
                thirty = costs[2] + dp[max(i - 30, 0)]

                dp[i] = min(one, seven, thirty)
            else:
                dp[i] = dp[i - 1]

        return dp[-1]