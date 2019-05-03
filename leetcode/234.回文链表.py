#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        last, curr, futu = None, head, head.next
        fast = head
        odd = False
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
                odd = True
            curr.next = last
            last = curr
            curr = futu
            if curr:
                futu = curr.next
        if odd:
            last = last.next
        while curr:
            if curr.val == last.val:
                curr = curr.next
                last = last.next
            else:
                return False
        return True


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
s = Solution()
s.isPalindrome(head)
