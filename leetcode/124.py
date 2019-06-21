# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        self.longest = root.val

        def lfr(root):
            if not root:
                return 0
            l, r = lfr(root.left), lfr(root.right)
            self.longest = max(self.longest, l+r+root.val)
            return 0 if root.val+max(l, r) < 0 \
                else root.val + max(l, r)

        lfr(root)
        return self.longest
