# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution0:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        last = fast = slow = head
        while fast:
            last = slow
            slow = slow.next
            fast = fast.next
            fast = fast.next if fast else fast
        if fast == slow:
            return head
        last.next = None
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
        if l1 or l2:
            curr.next = l1 if l1 else l2
        return dummy.next


nodes = [4, 2, 1, 3]
fast = dummy = ListNode(0)
for i in nodes:
    fast.next = ListNode(i)
    fast = fast.next
s = Solution()
ans = s.sortList(dummy.next)


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        last = slow = fast = head

        while fast:
            last = slow
            fast = fast.next
            slow = slow.next
            fast = fast.next if fast else fast

        l1 = head
        l2 = last.next
        last.next = None

        return self.merge(self.sortList(l1), self.sortList(l2))

    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
