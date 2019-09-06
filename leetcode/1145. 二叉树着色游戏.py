# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        if n == 1:
            # return not root.right == root.left
            return False

        def cnt(node):
            if not node:
                return 0
            return cnt(node.right)+cnt(node.left)+1

        l = collections.deque([root])
        while l:
            curr = l.popleft()
            if curr.val == x:
                break
            else:
                if curr.left:
                    l.append(curr.left)
                if curr.right:
                    l.append(curr.right)

        occ = cnt(curr)

        if occ == n:
            return cnt(curr.left) != cnt(curr.right)

        if occ > n//2:
            return max(cnt(curr.left), cnt(curr.right)) > n//2

        return True
