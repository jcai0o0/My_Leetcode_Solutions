class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        a = [0 for _ in range(N)]
        b = [0 for _ in range(N)]
        b[0] = nums[0]
        for i in range(1, N):
            a[i] = max(a[i-1], b[i-1])
            b[i] = a[i-1] + nums[i]

        return max(a[-1], b[-1])