# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left == right:
            return root
        else:
            return self.lcaDeepestLeaves(root.left) if left > right else \
                self.lcaDeepestLeaves(root.right)

    def depth(self, node):
        if not node:
            return 0
        return max(self.depth(node.right), self.depth(node.left))+1


class Solution1:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        curr_l = [root]
        next_l = []
        dest_l = []

        def bfs(curr_l, next_l, dest_l):
            for node in curr_l:
                if not node:
                    continue
                if not node.right:
                    next_l.append(node.right)
                if not node.left:
                    next_l.append(node.left)
            if not next_l:
                dest_l = curr_l
                return
            bfs(next_l, [], dest_l)

        bfs(curr_l, next_l, dest_l)

        dest_s = set(dest_l)

        path = []

        tree_root = TreeNode(root.val)
        # 未完成
        # def add_tree(path):
        #     curr = root
        #     for node in path:
        #         if node.val == curr.val:

        def bfs(node, path):
            if not node:
                return
            path.append(node)
            if node in dest_s:
                add_tree()
            bfs(node.right, path)
            bfs(node.left, path)
            path.pop()

        bfs(root, path)


class Solution_fail:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        d = {None: -1}

        def find_dept(d, node, l):
            if not node:
                return
            if not node.right and not node.left:
                d[node] = l
            if node.right not in d:
                find_dept(d, node.right, l+1)
            if node.left not in d:
                find_dept(d, node.left, l+1)
            if node not in d:
                if node.right and not node.left:
                    d[node] = d[node.right]
                elif node.left and not node.right:
                    d[node] = d[node.left]
                else:
                    d[node] = d[node.left] if d[node.left] == d[node.right]\
                        and d[node.left] != -1 and d[node.right] != -1 else -1

        find_dept(d, root, 0)

        self.res = root

        def bfs(q, d):
            if not q:
                return
            nq = []
            dept = 0
            for i, node in enumerate(q):
                if node.right:
                    nq.append(node.right)
                if node.left:
                    nq.append(node.left)
                if d[q[dept]] < d[node]:
                    dept = i
            if d[q[dept]] != -1:
                self.res = q[dept]
                if not (nq and not self.res.right and not self.res.left):
                    return
            bfs(nq, d)

        bfs([root], d)
        return self.res
