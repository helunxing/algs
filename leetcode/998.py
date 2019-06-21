# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoMaxTree(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        a = []

        def zhong(root):
            if not root:
                return
            zhong(root.left)
            a.append(root.val)
            zhong(root.right)

        zhong(root)

        a.append(val)

        def cre(b):
            if not b:
                return None
            max = 0
            for i in range(len(b)):
                if b[i] > b[max]:
                    max = i
            ans = TreeNode(b[max])
            ans.left = cre(b[:max])
            ans.right = cre(b[max+1:])
            return ans

        return cre(a)
