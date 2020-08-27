class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # if the intervals is empty or contain only one element return -1
        if not intervals or len(intervals) == 1:
            return [-1]
        # use res to store the final return
        # use dictionary start to store the index
        # use list start_list to store all the start point in the intervals
        res = []
        start = {}
        start_list = []

        # iterate through the intervals
        # store the start point and its index in dictionary start
        # store the start point in start_list
        for i in range(len(intervals)):
            start[intervals[i][0]] = i
            start_list.append(intervals[i][0])
        # sort start_list
        start_list = sorted(start_list)

        # iterate through the intervals
        # use the helper function (binary search) to find the first number that is larger than its end point
        for interval in intervals:
            first = self.helper(start_list, interval[1])
            res.append(-1 if first == -1 else start[start_list[first]])
        return res

    def helper(self, arr, num):
        # given an array start_list and an end point
        # return the index of the first number that is larger than end point, otherwise return -1
        left, right = 0, len(arr) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= num:
                right = mid - 1
                first = mid
            else:
                left = mid + 1
        return first