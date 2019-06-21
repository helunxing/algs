# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        curr = root
        stack = []
        ans = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                # 栈保存经过的运行点

            curr = stack[-1]
            del stack[-1]
            ans.append(curr.val)

            curr = curr.right

        return ans


class recusion:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.inord(root)
        return self.ans

    def inord(self, root):
        if not root:
            return
        self.inord(root.left)
        self.ans.append(root.val)
        self.inord(root.right)
