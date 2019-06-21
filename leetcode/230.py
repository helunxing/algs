# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        s = []
        count = 0
        while root or s:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            count += 1
            if count == k:
                return root.val
            root = root.right

    def kthSmallest_rec(self, root: TreeNode, k: int) -> int:
        self.count = 0

        def inord(root):
            if not root:
                return
            inord(root.left)
            self.count += 1
            if self.count == k:
                self.res = root.val
                return
            inord(root.right)

        inord(root)
        return self.res
