# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float('inf')
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0

        left = self.helper(node.left)
        right = self.helper(node.right)

        left = 0 if left < 0 else left
        right = 0 if right < 0 else right

        self.res = max(self.res, node.val + left + right)

        return max(left, right) + node.val