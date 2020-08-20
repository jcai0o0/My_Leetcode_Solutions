# my solution 112ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_1:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.res = False
        self.res = self.helper(root, arr, 0, len(arr))
        return self.res

    def helper(self, node, arr, idx, N):
        if not node:
            return False

        if node.val == arr[idx]:
            if idx == N - 1:  # the last idx
                if node.left or node.right:
                    return False
                elif not node.left and not node.right:
                    return True
            elif idx < N - 1:  # not reach the last idx yet
                if not node.left and not node.right:
                    return False
                else:
                    left_res = self.helper(node.left, arr, idx + 1, N)
                    right_res = self.helper(node.right, arr, idx + 1, N)
                    return (left_res or right_res)

        elif node.val != arr[idx]:
            return False


class Solution_2:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root is None:
            return len(arr) == 0

        def dfs(node, i):
            if not node.left and not node.right:
                return i == len(arr) - 1 and node.val == arr[i]
            if i >= len(arr) or node.val != arr[i]:
                return False
            res = False
            if node.left is not None:
                res = dfs(node.left, i + 1) or res
            if node.right is not None:
                res = dfs(node.right, i + 1) or res
            return res

        return dfs(root, 0)