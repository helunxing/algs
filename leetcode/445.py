# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 19
        a, s1, s2 = [], [], []
        r1, r2 = l1, l2

        while r1:
            s1.append(r1.val)
            r1 = r1.next
        while r2:
            s2.append(r2.val)
            r2 = r2.next

        last = 0
        while s1 or s2:
            if s1:
                one = s1[-1]
                del s1[-1]
            else:
                one = 0
            if s2:
                two = s2[-1]
                del s2[-1]
            else:
                two = 0

            pos = two+one+last
            last = pos//10
            pos %= 10

            a.append(pos)

        if last:  # 错误二
            a.append(last)

        dummy = ListNode(0)
        rear = dummy

        while a:
            rear.next = ListNode(a[-1])
            rear = rear.next  # 错误一
            del a[-1]

        return dummy.next
        # 33 finfish
        # 41 succes