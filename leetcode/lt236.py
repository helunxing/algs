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
        self.already = [root]
        self.not_yet = [root]
        curr = root
        self.p_stack = []
        self.q_stack = []

        while not len(self.p_stack) or not len(self.q_stack):

            if curr.val == p.val:
                self.p_stack = self.already[:]
            if curr.val == q.val:
                self.q_stack = self.already[:]

            if curr.left != None:
                self.not_yet.append(curr.right)
                self.already.append(curr.left)
                curr = curr.left
            elif curr.right != None:
                self.not_yet.append(curr.left)
                self.already.append(curr.right)
                curr = curr.right
            else:
                # if not curr.left and not curr.right:
                while self.not_yet[-1] == None:
                    del self.not_yet[-1]
                    del self.already[-1]
                curr = self.not_yet[-1]
                del self.not_yet[-1]
                del self.already[-1]
                self.already.append(curr)

        ans = root
        for i in range(min(len(self.p_stack), len(self.q_stack))):
            if self.p_stack[i].val == self.q_stack[i].val:
                ans = self.p_stack[i]
        return ans


class Solution_recursion_passed(object):
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
