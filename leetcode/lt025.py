# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        ance = dummy
        prev = dummy
        curr = dummy.next

        fron = dummy.next

        if curr == None or curr.next == None:  # 保证了链表至少有一个元素
            return dummy.next

        while True:
            for i in range(k):
                if fron == None:
                    return dummy.next
                fron = fron.next

            for i in range(k):
                foll = curr.next
                curr.next = prev
                prev = curr
                curr = foll

            ance.next.next = curr
            temp = prev
            prev = ance.next
            ance.next = temp

            ance = prev
    