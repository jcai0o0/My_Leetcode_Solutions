class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        curr = 0
        while candies > 0:
            res[curr % num_people] += min(candies, curr+1)
            curr += 1
            candies -= curr
        return res