# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1903:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 51
        dummy = ListNode(0)
        curr = dummy
        car, pos = 0, 0

        while l1 and l2:
            car, pos = divmod(car+l1.val+l2.val, 10)
            curr.next = ListNode(pos)
            curr, l1, l2 = curr.next, l1.next, l2.next

        if l1 or l2:
            rema = l1 if l1 else l2
            while rema:
                car, pos = divmod(car+rema.val, 10)
                curr.next = ListNode(pos)
                curr, rema = curr.next, rema.next

        if car:
            curr.next = ListNode(car)

        return dummy
        # 12


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


# s = Solution1903()

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
# ans = s.addTwoNumbers(l1, l2)
# pass

# l1 = ListNode(0)
# l2 = ListNode(1)
# l2.next = ListNode(2)
# ans = s.addTwoNumbers(l1, l2)
# pass

# l1 = ListNode(5)
# l2 = ListNode(5)
# ans = s.addTwoNumbers(l1, l2)
# pass
