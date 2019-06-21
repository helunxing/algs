# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        rela = {None:None}
        curr = head
        copy_dummy = RandomListNode(0)
        curr_copy = copy_dummy
        while curr != None:
            curr_copy.next = RandomListNode(curr.label)
            rela[curr] = curr_copy.next
            curr_copy = curr_copy.next
            curr = curr.next
        curr_copy.next = None

        curr = head
        curr_copy = copy_dummy.next
        while curr != None:
            curr_copy.random = rela[curr.random]
            curr = curr.next
            curr_copy = curr_copy.next

        return copy_dummy.next
