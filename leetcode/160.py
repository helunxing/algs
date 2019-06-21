# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1903(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        c1, c2 = headA, headB
        while c1 != c2:
            c1 = c1.next if c1 else headB
            c2 = c2.next if c2 else headA
        return c1


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr_a = headA
        curr_b = headB
        cou_a = 0
        cou_b = 0
        while curr_a:
            curr_a = curr_a.next
            cou_a += 1
        while curr_b:
            curr_b = curr_b.next
            cou_b += 1

        curr_a = headA
        curr_b = headB
        if cou_a-cou_b > 0:
            for i in range(cou_a-cou_b):
                curr_a = curr_a.next
        else:
            for i in range(cou_b-cou_a):
                curr_b = curr_b.next

        while curr_a != curr_b and curr_a and curr_b:
            curr_a = curr_a.next
            curr_b = curr_b.next
        if curr_a == curr_b:
            return curr_a
        else:
            return None
