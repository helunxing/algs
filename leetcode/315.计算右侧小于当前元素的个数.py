#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#


class Solution_give_up:
    def countSmaller(self, nums):
        # if not nums:
        #     return []
        # tail = [nums[-1]]
        # left = [0]

        # def bs(tar):
        #     # 找到第一个不大等于的数
        #     l, r = 0, len(tail)-1
        #     while l <= r:
        #         m = l+(r-l)//2
        #         # if nums[m]

        # for i in range(len(nums)-2, -1, -1):
        #     bs(nums[i])

        pass


class Solution_BST_amazon_error:
    def countSmaller(self, nums):
        self.res = [0]*len(nums)
        root = None
        for i in reversed(range(len(nums))):
            root = self.insertNode(root, nums[i], i)
        return self.res

    def insertNode(self, root, val, idx):
        if root:
            if val < root.val:
                root.count += 1
                root.left = self.insertNode(root.left, val, idx)
            else:
                # 需要累计所有比它小的节点的值，此处错误会导致仅记录最后一个经过的，
                # 并被放入右侧值的节点值，但在默认例中，与正确答案相同
                self.res[idx] = root.val
                root.right = self.insertNode(root.right, val, idx)
        else:
            root = BST_Node(val)
        return root


class Solution_BST:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.res = [0]*len(nums)
        root = None
        for i in reversed(range(len(nums))):
            root = self.insertNode(root, nums[i], i)
        return self.res

    def insertNode(self, root, val, idx):
        if root:
            # 如果等于，放在左边，不累计当前节点的小于情况，避免累计相等的节点
            if val <= root.val:
                root.count += 1
                root.left = self.insertNode(root.left, val, idx)
            else:
                # 需要累计所有比它小的节点的值
                self.res[idx] += root.count+1
                root.right = self.insertNode(root.right, val, idx)
        else:
            root = BST_Node(val)
        return root


class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 0


s = Solution_BST()
s.countSmaller([5, 2, 6, 1])
