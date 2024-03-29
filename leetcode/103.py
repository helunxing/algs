# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        shift = False
        dq = [root]
        nq = []
        while dq:
            tmp = []
            for n in dq:
                tmp.append(n.val)
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            if shift:
                ans.append(list(reversed(tmp)))
            else:
                ans.append(tmp)
            shift = not shift
            dq = nq
            nq = []
        return ans


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ans = []
        tmp = []

        def bfs(lev):
            q = []
            nums = []
            if not lev:
                if root:
                    q.append(root)
                    nums.append(root.val)
            elif lev & 1:
                for i in range(len(tmp[-1])-1, -1, -1):
                    if tmp[-1][i].right:
                        q.append(tmp[-1][i].right)
                        nums.append(tmp[-1][i].right.val)
                    if tmp[-1][i].left:
                        q.append(tmp[-1][i].left)
                        nums.append(tmp[-1][i].left.val)
            else:
                for i in range(len(tmp[-1])-1, -1, -1):
                    if tmp[-1][i].left:
                        q.append(tmp[-1][i].left)
                        nums.append(tmp[-1][i].left.val)
                    if tmp[-1][i].right:
                        q.append(tmp[-1][i].right)
                        nums.append(tmp[-1][i].right.val)
            if q:
                tmp.append(q)
                ans.append(nums)
                bfs(lev+1)

        bfs(0)

        return ans


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
s = Solution()
s.zigzagLevelOrder(node)
