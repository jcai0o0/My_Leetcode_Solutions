class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        f = [0] * N
        g = [0] * N
        f[0] = g[0] = res = nums[0]
        for i in range(1, N):
            f[i] = max(f[i-1] * nums[i], nums[i], g[i-1] * nums[i])
            g[i] = min(f[i-1] * nums[i], nums[i], g[i-1] * nums[i])
            res = max(res, f[i])
        return res