class Solution_1:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        if root.val == key:
            if not root.right:
                left = root.left
                return left
            else:
                right = root.right
                while right.left:
                    right = right.left
                root.val, right.val = right.val, root.val
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root

class Solution_2:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            else:
                temp = root.right
                while temp.left:
                    temp = temp.left

                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root