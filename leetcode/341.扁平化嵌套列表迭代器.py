#
# @lc app=leetcode.cn id=341 lang=python
#
# [341] 扁平化嵌套列表迭代器
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        curr, idx = self.stack[-1]
        self.stack[-1][1] += 1
        return curr[idx].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            curr, idx = s[-1]
            if idx == len(curr):
                s.pop()
                continue
            x = curr[idx]
            if x.isInteger():
                return True
            s[-1][1] += 1
            s.append([x.getList(), 0])
        return False


class NestedIterator_rec_give_up(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.curr = nestedList
        self.idx = 0

    def next(self):
        """
        :rtype: int
        """
        # 需要得到上层的状态
        if len(self.curr) <= self.idx:
            return NestedIterator(self.curr[self.idx].next())
        else:
            if self.curr[self.idx].isInteger():
                ret = self.curr[self.idx].getInteger()
                self.idx += 1
            else:
                ret = NestedIterator(self.curr[self.idx]).next()
            return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.curr) <= self.idx:
            return False
        else:
            return True if self.curr[self.idx].isInteger() else \
                NestedIterator(self.curr[self.idx]).hasNext()


class NestedIterator_pochmann(object):

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False


class NestedIterator_rec_use_reference(object):

    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.index = 0
        self.temp_nested_list = None
        self.length = len(self.nestedList)

    def next(self):
        if self.temp_nested_list:
            return self.temp_nested_list.next()
        else:
            self.index += 1
            return self.nestedList[self.index - 1].getInteger()

    def hasNext(self):
        if self.index >= self.length:
            return False
        elif self.temp_nested_list:  # 如果临时变量为嵌套迭代器
            if self.temp_nested_list.hasNext():  # 且拥有下一个整数
                return True  # 此时next()会返回嵌套迭代器的next()整数
            else:
                self.temp_nested_list = None  # 否则置空索引+1重新判断
                self.index += 1
                return self.hasNext()
        else:  # 临时变量为空
            if self.nestedList[self.index].isInteger():  # 当前索引元素为整数，next直接返回索引整数且索引+1
                return True
            else:  # 当前索引元素为嵌套，临时变量赋值为嵌套迭代器对象
                self.temp_nested_list = NestedIterator(
                    self.nestedList[self.index].getList())
                return self.hasNext()  # 重新调用判断

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
