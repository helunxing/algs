class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)

        while head:
            curr = head
            head = head.next
            ins = dummy
            while ins.next and ins.next.val < curr.val:
                ins = ins.next
            curr.next = ins.next
            ins.next = curr

        return dummy.next
