#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution0:
    def oddEvenList(self, head: ListNode) -> ListNode:
        o_d, e_d = ListNode(0), ListNode(0)
        curr = head
        o, e = o_d, e_d
        now = o

        while curr:
            now.next = curr
            if now == o:
                o = o.next
                now = e
            else:
                e = e.next
                now = o
            curr = curr.next
        e.next = None
        o.next = e_d.next
        return o_d.next


# dummy = ListNode(0)
# head = dummy
# l = [1, 2, 3, 4, 5]
# for i in l:
#     head.next = ListNode(i)
#     head = head.next
# s = Solution()
# s.oddEvenList(dummy.next)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        odd, eve = ListNode(0), ListNode(0)
        o, e = odd, eve
        curr = head
        l_o = True

        while curr:
            if l_o:
                o.next = curr
                o = o.next
            else:
                e.next = curr
                e = e.next
            curr = curr.next
            l_o = not l_o

        e.next = None
        o.next = eve.next
        return odd.next
