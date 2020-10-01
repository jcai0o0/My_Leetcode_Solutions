class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        temp = []
        for n, start, end in trips:
            temp.append((start, n))
            temp.append((end, -n))
        temp.sort()
        par = 0
        for i in temp:
            par += i[1]
            if par > capacity:
                return False
        return True