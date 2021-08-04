# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 非递归
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:

        curr, tail = None, head

        while tail:
            n = tail.next
            tail.next = curr
            curr = tail
            tail = n

        return curr


# 递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        new_head=self.reverseList(head.next)

        head.next.next=head
        head.next=None

        return new_head
