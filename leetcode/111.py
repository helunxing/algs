# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.right:
            return 1+self.minDepth(root.left)
        if not root.left:
            return 1+self.minDepth(root.right)

        return 1+min(self.minDepth(root.right), self.minDepth(root.left))
