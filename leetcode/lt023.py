# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution1903:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(h1, h2):
            dummy = curr = ListNode(0)
            while h1 and h2:
                if h1.val > h2.val:
                    curr.next, h2 = h2, h2.next
                    curr = curr.next
                else:
                    curr.next, h1 = h1, h1.next
                    curr = curr.next
            if h1 or h2:
                rem = h1 if h1 else h2
                curr.next = rem
            return dummy.next

        while len(lists) > 1:
            tmp = merge(lists[0], lists[1])
            del lists[0]
            del lists[0]
            lists.append(tmp)
        return lists[0] if lists else []


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
