# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
# 就是不停地在收据信啊，感觉一点希望都没有，叹气

class Solution:
    def rand49(self):
        return 7 * (rand7() - 1) + rand7() - 1

    def rand10(self):
        """
        :rtype: int
        """
        num = self.rand49()
        while num > 39:
            num = self.rand49()
        return num % 10 + 1