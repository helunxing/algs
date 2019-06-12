# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        dummy = TreeNode(0)
        dummy.left = root
        self.d = {None: 0}

        def build(node):
            if not node:
                return
            build(node.right)
            build(node.left)
            self.d[node] = max(self.d[node.right], self.d[node.left])+node.val

        def search(node, s):
            if not node:
                return
            if self.d[node.right]+s+node.val < limit:
                node.right = None
            if self.d[node.left]+s+node.val < limit:
                node.left = None
            search(node.right, s+node.val)
            search(node.left, s+node.val)

        build(dummy)
        search(dummy, 0)

        return dummy.left
