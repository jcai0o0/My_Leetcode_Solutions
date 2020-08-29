class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.area = [0] * (len(rects) + 1)
        for i in range(1, len(rects) + 1):
            rect = rects[i - 1]
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.area[i] = self.area[i - 1] + area

    def pick(self) -> List[int]:
        d = random.randint(1, self.area[-1])
        left, right = 1, len(self.rects)
        index = 0
        while left <= right:
            m = (left + right) // 2
            if d <= self.area[m] and d > self.area[m - 1]:
                index = m - 1
                break
            if d > self.area[m]:
                left = m + 1
            else:
                right = m - 1
        xleft, xright = self.rects[index][0], self.rects[index][2]
        yleft, yright = self.rects[index][1], self.rects[index][3]
        x = random.randint(xleft, xright)
        y = random.randint(yleft, yright)
        return [x, y]