# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        curr = head
        l, h = ListNode(0), ListNode(0)
        lc, hc = l, h
        while curr:
            if curr.val < x:
                lc.next = curr
                lc = lc.next
            else:
                hc.next = curr
                hc = hc.next
            curr = curr.next
        hc.next = None
        lc.next = h.next
        return l.next
