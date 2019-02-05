# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        for i in range(len(lists)-1, -1, -1):
            if not lists[i]:
                del lists[i]
        ans = ListNode(0)
        curr = ans
        while lists:
            min_ = 0
            for i in range(len(lists)):
                if lists[i].val < lists[min_].val:
                    min_ = i
            curr.next = lists[min_]
            curr = curr.next
            lists[min_] = lists[min_].next
            if not lists[min_]:
                del lists[min_]
        return ans.next


s = Solution()
a = [None, None]
s.mergeKLists(a)
pass
