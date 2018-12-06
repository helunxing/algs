# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.creat_sub_BST(nums, 0, len(nums)-1)

    def creat_sub_BST(self, nums, front, rear):
        if front > rear:
            return None
        mid = front+(rear-front)//2
        node = TreeNode(nums[mid])
        node.left = self.creat_sub_BST(nums, front, mid-1)
        node.right = self.creat_sub_BST(nums, mid+1, rear)
        return node
