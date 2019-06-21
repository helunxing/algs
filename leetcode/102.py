# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.stack=[]
        self.fromSNode(root, 0)
        return self.stack

    stack = []

    def fromSNode(self, node, level):
        if node == None:
            return
        else:
            if len(self.stack) < level+1:
                self.stack.append([])
            self.stack[level].append(node.val)

        if node.left != None:
            self.fromSNode(node.left, level+1)
        if node.right != None:
            self.fromSNode(node.right, level+1)
