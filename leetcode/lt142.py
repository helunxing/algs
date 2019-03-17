# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1903(object):
    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cou_fri = 0
        cou_sec = 0
        poi_fri = head
        poi_sec = head
        while True:
            if poi_sec == None or poi_sec.next == None:
                return None

            poi_fri = poi_fri.next
            poi_sec = poi_sec.next.next
            cou_fri += 1
            cou_sec += 2

            if poi_fri == poi_sec:
                break

        pos = 0

        poi_fri = head
        steps = cou_sec-cou_fri*2

        if steps > 0:
            pos += steps
            for i in range(steps):
                poi_fri = poi_fri.next
        else:
            for i in range(-steps):
                poi_sec = poi_sec.next

        while poi_fri != poi_sec:
            poi_fri = poi_fri.next
            poi_sec = poi_sec.next

        return poi_fri


dummy = ListNode(0)
fron = dummy

for i in [0, 1, 2, 3]:
    fron.next = ListNode(i)
    if i == 0:
        pod = fron.next
    fron = fron.next

fron.next = pod

s = Solution()
print(s.detectCycle(dummy.next).val)
