class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = {}
        for n in nums:
            if n in check:
                check[n] += 1
            else:
                check[n] = 1

        for key, freq in check.items():
            if freq == 1:
                return key