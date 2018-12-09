# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next != None and prev.next.next != None:
            front = prev.next
            rear = front.next
            front.next = rear.next
            rear.next = front
            prev.next = rear
            prev = front
            # 操作前需要记录上一个操作的结尾，以便修改其指向
            # 结尾需要将尾部移到正确的位置
        return dummy.next
