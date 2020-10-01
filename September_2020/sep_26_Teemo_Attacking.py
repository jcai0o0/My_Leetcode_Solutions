class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i in range(len(timeSeries)):
            t = timeSeries[i] + duration - 1
            if i == len(timeSeries)-1 or t < timeSeries[i+1]:
                res += duration
            else:
                res += (timeSeries[i+1] - timeSeries[i])
        return res