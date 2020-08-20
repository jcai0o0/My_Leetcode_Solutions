class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right - 1:
            mid = (left + right) // 2
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid + 1
        return left if isBadVersion(left) == True else right