class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        for num in nums:
            idx = abs(num)
            if nums[idx - 1] > 0:
                nums[idx - 1] *= -1

        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                return i
        return len(nums) + 1