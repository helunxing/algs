# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 极端值，数组长度为一或空
        curr, l = head, 0
        while curr:
            l += 1
            curr = curr.next

        if l < 2:
            return head

        fast = slow = head
        step = k % l

        for i in range(step):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        newhead = slow.next
        slow.next = None

        return newhead
