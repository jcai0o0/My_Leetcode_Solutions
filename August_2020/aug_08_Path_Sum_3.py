# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def helper(self, root, sum):
        res = 0
        if not root:
            return res
        sum -= root.val
        if sum == 0:
            res += 1
        res += self.helper(root.left, sum)
        res += self.helper(root.right, sum)
        return res