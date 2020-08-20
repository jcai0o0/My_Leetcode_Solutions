class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        prod = 1
        for i in range(n):
            ans.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(n-1, -1, -1):
            ans[i] *= prod
            prod *= nums[i]
        return ans