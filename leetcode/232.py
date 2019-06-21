class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_s = []
        self.out_s = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.in_s.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.out_s) == 0:
            if self.empty():
                return
            self.move()
        temp = self.out_s[-1]
        del self.out_s[-1]
        return temp

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.out_s) == 0:
            if self.empty():
                return 0
            self.move()
        return self.out_s[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.in_s) == 0 and len(self.out_s) == 0:
            return True
        else:
            return False

    def move(self):
        while len(self.in_s) != 0:
            self.out_s.append(self.in_s[-1])
            del self.in_s[-1]


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
