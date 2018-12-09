class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return head
        # 删除本行反而会变慢

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(m-1):
            prev = prev.next
        start = prev
        front = prev.next
        for i in range(n-m+1):
            rear = front.next
            front.next = prev
            prev = front
            front = rear
        start.next.next = rear
        start.next = prev
        return dummy.next  # 防止翻转至结尾
