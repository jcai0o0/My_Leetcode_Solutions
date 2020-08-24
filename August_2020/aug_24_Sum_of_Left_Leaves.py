# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(N)
# Space complexity: O(N)
class Solution_1_recursion:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        self.helper(root)
        return self.sum

    def helper(self, root):
        if not root:
            return
        if root.left and not root.left.left and not root.left.right:
            self.sum += root.left.val

        self.helper(root.right)
        self.helper(root.left)

class Solution_2_recursion:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)