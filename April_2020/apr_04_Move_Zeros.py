class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums
        p = 0
        r = 1
        while r < len(nums):
            if nums[p] == 0 and nums[r] != 0:
                nums[p], nums[r] = nums[r], nums[p]
                p += 1
                r += 1
            elif nums[p] == 0 and nums[r] == 0:
                r += 1
            else:
                p += 1
                r += 1
        return nums