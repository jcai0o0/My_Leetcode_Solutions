# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        res = -1
        n, m = binaryMatrix.dimensions()
        x, y = 0, m-1
        while x < n and  y >= 0:
            if binaryMatrix.get(x, y) == 1:
                res = y
                y -= 1
            else:
                x += 1
        return res