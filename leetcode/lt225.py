class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_q = []
        self.vice_q = []

    def move(self):
        while len(self.main_q) > 1:
            self.vice_q.append(self.main_q[0])
            del self.main_q[0]

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.main_q.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.main_q) == 0:
            if self.empty():
                return 0
        self.move()
        temp = self.main_q[0]
        del self.main_q[0]
        self.main_q, self.vice_q = self.vice_q, self.main_q
        return temp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.main_q) == 0:
            if self.empty():
                return 0
        self.move()
        temp = self.main_q[0]
        del self.main_q[0]
        self.vice_q.append(temp)
        self.main_q, self.vice_q = self.vice_q, self.main_q
        return temp

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.main_q) == 0 and len(self.vice_q) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
