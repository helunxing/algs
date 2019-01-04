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
