#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

import collections
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(set)
        self.l = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.d[val].add(len(self.l))
        self.l.append(val)
        return len(self.d[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.d[val]) == 0:
            return False
        index = self.d[val].pop()
        self.l[index] = self.l[-1]
        self.d[self.l[-1]].add(index)
        self.d[self.l[-1]].remove(len(self.l)-1)
        self.l.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if not self.l:
            return 0
        return self.l[random.randrange(0, len(self.l))]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

["RandomizedCollection", "insert", "insert",
    "remove", "insert", "remove", "getRandom"]
[[], [0], [1], [0], [2], [1], []]

["RandomizedCollection", "insert", "insert",
    "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]

["RandomizedCollection", "insert", "insert", "insert",
    "insert", "insert", "remove", "remove", "remove", "remove"]
[[], [4], [3], [4], [2], [4], [4], [3], [4], [4]]

["RandomizedCollection", "insert", "insert", "insert", "insert", "insert",
 "insert", "remove", "remove", "remove", "remove", "getRandom", "getRandom",
 "getRandom", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom",
 "getRandom", "getRandom"]
[[], [1], [1], [2], [1], [2], [2], [1], [2], [2],
    [2], [], [], [], [], [], [], [], [], [], []]
