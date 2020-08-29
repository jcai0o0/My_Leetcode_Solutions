class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1, 1]
        if rowIndex == 0:
            return [1]
        i = 1
        while i <= rowIndex:
            new_res = [1] * (i+1)
            for j in range(1, len(new_res)-1):
                new_res[j] = res[j-1] + res[j]
            res = new_res
            i += 1
        return res

# time complexity : O(n)
# space complecity : O(n)