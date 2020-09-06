class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list_1, list_2 = [], []
        self.traverse(root1, list_1)
        self.traverse(root2, list_2)
        res = []
        i = j = 0
        while i < len(list_1) and j < len(list_2):
            if list_1[i] <= list_2[j]:
                res.append(list_1[i])
                i += 1
            else:
                res.append(list_2[j])
                j += 1
        if i < len(list_1):
            res.extend(list_1[i:])
        if j < len(list_2):
            res.extend(list_2[j:])
        return res

    def traverse(self, node, arr):
        if not node:
            return
        self.traverse(node.left, arr)
        arr.append(node.val)
        self.traverse(node.right, arr)