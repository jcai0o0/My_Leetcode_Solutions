class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = [0]
        if not root:
            return 0
        curr = str(root.val)
        self.helper(root, res, curr)
        return res[0]

    def helper(self, node, res, curr):
        if not node.left and not node.right:
            res[0] += int(curr, 2)
            return
        if node.left:
            curr += str(node.left.val)
            self.helper(node.left, res, curr)
            curr = curr[:-1]
        if node.right:
            curr += str(node.right.val)
            self.helper(node.right, res, curr)
            curr = curr[:-1]