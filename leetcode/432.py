class Node:
    """
    定义双向链表的节点 双向链表用于按顺序存储(key,value)
    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = dict()  # 用于存储key与双向链表中node(key,node)映射关系
        self.head = Node("", -1)  # 头节点 存储最小值
        self.tail = Node("", -1)  # 尾节点 存储最大值
        # 初始化双向链表
        self.tail.prev = self.head
        self.head.next = self.tail

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        # 新增key,插入到numDict中,并放置在双向链表head->next
        if key not in self.keys:
            insNode = Node(key, 1)
            self.keys[key] = insNode
            insNode.next = self.head.next
            self.head.next.prev = insNode
            self.head.next = insNode
            insNode.prev = self.head
        else:
            # 存量key
            curNode = self.keys[key]
            curNode.val += 1
            # 通过交换节点的方式保持双向链表有序
            while curNode.next != self.tail and curNode.val > curNode.next.val:
                prevNode = curNode.prev
                nextnextNode = curNode.next.next
                prevNode.next = curNode.next
                prevNode.next.prev = prevNode
                prevNode.next.next = curNode
                curNode.prev = prevNode.next
                curNode.next = nextnextNode
                nextnextNode.prev = curNode

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.keys:
            return
        curNode = self.keys[key]
        if curNode.val == 1:
            # 在双向链表中删除该节点
            prevNode = curNode.prev
            nextNode = curNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
        else:
            # 该key对应的value减1 并通过交换节点的方式保持双向链表有序
            curNode.val -= 1
            while curNode.prev != self.head and curNode.val < curNode.prev.val:
                prepreNode = curNode.prev.prev
                nextNode = curNode.next
                nextNode.prev = curNode.prev
                curNode.prev.prev = curNode
                curNode.prev = prepreNode
                curNode.next = nextNode.prev
                nextNode.prev.next = nextNode
                prepreNode.next = curNode

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.tail.prev.key if self.tail.prev != self.head else ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.head.next.key if self.head.next != self.tail else ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
