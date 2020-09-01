# we can iterate every minute from 23:59 (the largest) to 00:00 (the smallest)
# if we find the time that has the same 4 digits as the given array, we can return it
# time complexity : O(24 * 60)
# space complexity : O(1)
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A = sorted(A)
        for hour in range(23, -1, -1):
            for minute in range(59, -1, -1):
                temp = [hour//10, hour%10, minute//10, minute%10]
                sorted_temp = sorted(temp)
                if sorted_temp == A:
                    return str(temp[0]) + str(temp[1]) + ":" + str(temp[2]) + str(temp[3])
        return ""