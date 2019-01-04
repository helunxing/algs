# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ans = root
        self.p = p
        self.q = q

        self.find(root)

        return self.ans

    def find(self, curr):
        if curr == None:
            return False

        left = self.find(curr.left)
        right = self.find(curr.right)

        if curr.val == self.p.val or curr.val == self.q.val:
            if left or right:
                self.ans = curr
            return True
        else:
            if left and right:
                self.ans = curr

        return left or right


s = Solution()


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
print(s.lowestCommonAncestor(root, TreeNode(5), TreeNode(1)).val)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(3)).val)

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
print(s.lowestCommonAncestor(root, TreeNode(5), TreeNode(1)).val)


#   left    right|
#   have    have |curr=left,not_yet+right
#   None    None |if not_yet[-1]!= None curr=-1 else
#   have    None |curr=left,not_yet+None
#   None    have |curr=right,not_yet+None
