class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cur_sum = 0
        sum_dict = {0:1}
        for num in nums:
            cur_sum += num
            if cur_sum-k in sum_dict:
                ans += sum_dict[cur_sum-k]
            sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1
        return ans