class MinStack1903:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.m = 0

    def empty(self):
        return not self.s

    def push(self, x: int) -> None:
        if self.empty() or x <= self.m:
            self.s.append(self.m)
            self.m = x
        self.s.append(x)

    def pop(self) -> None:
        if self.s.pop() == self.m:
            self.m = self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m


class MinStack1903_fail:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = 0
        self.s = []

    def push(self, x: int) -> None:
        if len(self.s):
            self.s.append(x-self.min)
            if x < self.min:
                self.min = x
        else:
            self.min = x
            self.s.append(x-self.min)

    def pop(self) -> None:
        if not len(self.s):
            return
        if self.s[-1] < 0:
            self.min = self.min-self.s[-1]
        self.s.pop()

    def top(self) -> int:
        if not len(self.s):
            return 0
        if self.s[-1] >= 0:
            return self.s[-1]+self.min
        else:
            self.min = self.min-self.s[-1]
            return self.min+self.s[-1]

    def getMin(self) -> int:
        return self.min


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_s = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.min = x
        else:
            self.min = self.min_s[-1]
            if x < self.min:
                self.min = x
        self.stack.append(x)
        self.min_s.append(self.min)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            del self.stack[-1]
            del self.min_s[-1]
        # else:
        #     throw

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return 0

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.min_s[-1]
        else:
            return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
