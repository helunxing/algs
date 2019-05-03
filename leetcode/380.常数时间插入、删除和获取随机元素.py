#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        self.l[self.d[val]] = self.l[len(self.l)-1]
        self.d[val], self.d[self.l[len(self.l)-1]] = \
            self.d[self.l[len(self.l)-1]], self.d[val]
        self.l.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.l:
            return self.l[random.randrange(0, len(self.l))]
        return 0


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
