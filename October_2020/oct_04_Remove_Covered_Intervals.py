class Solution_1:
    # for every interval in arr, traverse the entire array to see if it's covered
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        for i, interval in enumerate(intervals):
            fir = interval[0]
            sec = interval[1]
            temp = 0
            for j in range(len(intervals)):
                if j == i:
                    continue
                if intervals[j][0]<=fir and sec <= intervals[j][1]:
                    temp += 1
            if temp == 0:
                res += 1
        return res

class Solution_2:
    # sort + traverse the entire array only once
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]

        for i in range(1, len(intervals)):
            temp = intervals[i]
            if left <= temp[0] and temp[1] <= right:
                cnt += 1
            elif temp[0] <= right and temp[1] >= right:
                right = temp[1]
            elif temp[0] > right:
                left = temp[0]
                right = temp[1]

        return len(intervals) - cnt