class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        ret = float('-inf')
        for i in range(len(nums)):
            if i == 0:
                res = nums[i]
            else:
                res = max(res+nums[i], nums[i])
            ret = max(ret, res)
        return ret