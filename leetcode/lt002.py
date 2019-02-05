# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        c2 = l2
        last = 0
        ans = ListNode(0)
        sum = ans
        while c1 != None or c2 != None:
            v1 = c1.val if c1 != None else 0
            v2 = c2.val if c2 != None else 0
            c1 = c1.next if c1 != None else None
            c2 = c2.next if c2 != None else None
            sum.next = ListNode((v1+v2+last) % 10)
            last = (v1+v2+last)//10
            sum = sum.next
        if last:
            pre = ans
            while pre.next:
                pre = pre.next
            pre.next = ListNode(last)
        return ans.next


s = Solution()

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# l1 = ListNode(0)
# l2 = ListNode(1)
# l2.next = ListNode(2)

l1 = ListNode(5)
l2 = ListNode(5)
s.addTwoNumbers(l1, l2)
