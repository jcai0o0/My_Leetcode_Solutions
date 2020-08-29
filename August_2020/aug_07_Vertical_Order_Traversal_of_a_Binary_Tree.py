# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cmp_to_key


class Solution:
    @staticmethod
    def compare_func(a, b):
        if a[0] < b[0]:
            return a[0] - b[0]
        elif a[0] == b[0]:
            return a[1] - b[1]
        return a[0] - b[0]

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur_line = [(root, (0, 0))]
        nxt_line = []
        res = []
        dic = defaultdict(list)
        while cur_line:
            pair = cur_line.pop(0)
            cur_node = pair[0]
            x = pair[1][0]
            y = pair[1][1]
            if cur_node.left:
                nxt_line.append((cur_node.left, (x - 1, y + 1)))
            if cur_node.right:
                nxt_line.append((cur_node.right, (x + 1, y + 1)))

            dic[x].append((y, cur_node.val))

            if len(cur_line) == 0:
                cur_line = nxt_line
                nxt_line = []

        # print(dic)
        for i in sorted(dic):
            cur = dic[i]
            print(cur)
            if len(cur) == 1:
                for t in cur:
                    res.append([t[1]])
            else:
                temp = []
                for t in sorted(dic[i], key=cmp_to_key(self.compare_func)):
                    temp.append(t[1])
                res.append(temp)
        return res