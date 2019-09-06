# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        # self.d = {None: (0, 0)}
        self.res = 0
        n, s = 0, 1

        def dfs(node):
            if not node:
                return (0, 0)
            r, l = dfs(node.right), dfs(node.left)
            su, nu = r[s]+l[s] + node.val, r[n]+l[n]+1
            self.res = max(self.res, su/nu)
            return (nu, su)

        dfs(root)
        return self.res
