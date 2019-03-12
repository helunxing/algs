# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        l = len(preorder)

        def creHead(sta, end):
            if l <= sta or l < end:
                return None
            if end <= sta:
                return None
            head = TreeNode(preorder[sta])
            # k是分界元素
            k = end
            for i in range(sta, end):
                if preorder[i] and preorder[i] > preorder[sta]:
                    k = i
                    break
            if k == end:
                # 如果最后为空，且左边全是小的，则右子树为空
                head.left = creHead(sta+1, end)
            else:
                # 如果第一个就比父母大，则后面都是右子树
                head.left = creHead(sta+1, k)
                head.right = creHead(k, end)

            return head

        return creHead(0, l)
