class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total_sum = 0
        dic = {0: -1}
        res = 0

        for i, num in enumerate(nums):
            if num == 0:
                total_sum -= 1
            else:
                total_sum += 1

            if total_sum in dic:
                res = max(res, i - dic[total_sum])
            else:
                dic[total_sum] = i
        return res