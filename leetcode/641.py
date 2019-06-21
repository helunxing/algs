class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.a = [0]*k
        self.l, self.f, self.r = 0, -1, 0
        self.k = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.l += 1
        self.a[self.f] = value
        self.f -= 1
        self.f %= self.k
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.l += 1
        self.a[self.r] = value
        self.r += 1
        self.r %= self.k
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.l -= 1
        self.f += 1
        self.f %= self.k
        self.a[self.f] = 0
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.l -= 1
        self.r -= 1
        self.r %= self.k
        self.a[self.r] = 0
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.a[(self.f+1) % self.k]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.a[(self.r-1) % self.k]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.l <= 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.l >= self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
