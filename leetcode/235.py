# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor_1903(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if not root:
            return root
        elif p.val == root.val or root.val == q.val \
                or p.val <= root.val <= q.val:
            return root
        else:
            if p.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return self.lowestCommonAncestor(root.left, p, q)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        queue_p = []
        queue_q = []
        poi_p = root
        poi_q = root
        while poi_p != None:
            queue_p.append(poi_p)
            if poi_p.val == p.val:
                poi_p = None
            elif poi_p.val > p.val:
                poi_p = poi_p.left
            elif poi_p.val < p.val:
                poi_p = poi_p.right

        while poi_q != None:
            queue_q.append(poi_q)
            if poi_q.val == q.val:
                poi_q = None
            elif poi_q.val > q.val:
                poi_q = poi_q.left
            elif poi_q.val < q.val:
                poi_q = poi_q.right

        ans = root
        for i in range(min(len(queue_p), len(queue_q))):
            if queue_p[i].val == queue_q[i].val:
                ans = queue_p[i]

        return ans
