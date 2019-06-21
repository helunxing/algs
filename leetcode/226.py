# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        # 02
        def exc(root):
            if not root:
                return
            root.right, root.left = root.left, root.right
            exc(root.right)
            exc(root.left)
        exc(root)
        return root
        # 06
