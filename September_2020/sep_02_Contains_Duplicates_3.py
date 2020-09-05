class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k <= 0 or t < 0:
            return False
        dic = {}
        for i, num in enumerate(nums):
            key = num // (t + 1)
            if key in dic or (key+1 in dic and dic[key+1]-num <= t) or (key-1 in dic and num-dic[key-1] <= t):
                return True
            if i >= k:
                del dic[nums[i-k] // (t + 1)]
            dic[key] = num
        return False