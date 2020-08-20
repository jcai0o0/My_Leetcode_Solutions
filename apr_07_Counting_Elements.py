class Solution:
    def countElements(self, arr: List[int]) -> int:
        check = {}
        for num in arr:
            if num in check:
                check[num] += 1
            else:
                check[num] = 1
        count = 0
        for key in check.keys():
            if key+1 in check.keys():
                count += check[key]
        return count