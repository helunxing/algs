class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.k = k
        self.a = [0]*k
        self.l, self.r, self.f = 0, 0, 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.l >= self.k:
            return False
        self.a[self.r] = value
        self.l += 1
        self.r += 1
        self.r %= self.k
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.l <= 0:
            return False
        self.a[self.f] = 0
        self.l -= 1
        self.f += 1
        self.f %= self.k
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.l:
            return self.a[self.f]
        else:
            return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.l:
            return self.a[(self.r-1) % self.k]
        else:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.l <= 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.l >= self.k


# Your MyCircularQueue object will be instantiated and called as such:
k = 5
obj = MyCircularQueue(k)
p1 = obj.enQueue(1)
p2 = obj.deQueue()
p4 = obj.enQueue(2)
p3 = obj.enQueue(3)
p5 = obj.deQueue()
pass
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# ["MyCircularQueue","enQueue","deQueue","enQueue","enQueue","deQueue","isFull","isFull","Front","deQueue","enQueue","Front","enQueue","enQueue","Rear","Rear","deQueue","enQueue","enQueue","Rear","Rear","Front","Rear","Rear","deQueue","enQueue","Rear","deQueue","Rear","Rear","Front","Front","enQueue","enQueue","Front","enQueue","enQueue","enQueue","Front","isEmpty","enQueue","Rear","enQueue","Front","enQueue","enQueue","Front","enQueue","deQueue","deQueue","enQueue","deQueue","Front","enQueue","Rear","isEmpty","Front","enQueue","Front","deQueue","enQueue","enQueue","deQueue","deQueue","Front","Front","deQueue","isEmpty","enQueue","Rear","Front","enQueue","isEmpty","Front","Front","enQueue","enQueue","enQueue","Rear","Front","Front","enQueue","isEmpty","deQueue","enQueue","enQueue","Rear","deQueue","Rear","Front","enQueue","deQueue","Rear","Front","Rear","deQueue","Rear","Rear","enQueue","enQueue","Rear","enQueue"]
# [[81],[69],[],[92],[12],[],[],[],[],[],[28],[],[13],[45],[],[],[],[24],[27],[],[],[],[],[],[],[88],[],[],[],[],[],[],[53],[39],[],[28],[66],[17],[],[],[47],[],[87],[],[92],[94],[],[59],[],[],[99],[],[],[84],[],[],[],[52],[],[],[86],[30],[],[],[],[],[],[],[45],[],[],[83],[],[],[],[22],[77],[23],[],[],[],[14],[],[],[90],[57],[],[],[],[],[34],[],[],[],[],[],[],[],[49],[59],[],[71]]
# [null,true,true,true,true,true,false,false,92,true,true,0,true,true,45,45,true,true,true,27,27,12,27,27,true,true,88,true,88,88,13,13,true,true,13,true,true,true,13,false,true,47,true,13,true,true,13,true,true,true,true,true,27,true,84,false,27,true,27,true,true,true,true,true,39,39,true,false,true,45,28,true,false,28,28,true,true,true,23,28,28,true,false,true,true,true,57,true,57,17,true,true,34,47,34,true,34,34,true,true,59,true]
# [null,true,true,true,true,true,false,false,12,true,true,28,true,true,45,45,true,true,true,27,27,13,27,27,true,true,88,true,88,88,24,24,true,true,24,true,true,true,24,false,true,47,true,24,true,true,24,true,true,true,true,true,53,true,84,false,53,true,53,true,true,true,true,true,66,66,true,false,true,45,17,true,false,17,17,true,true,true,23,17,17,true,false,true,true,true,57,true,57,87,true,true,34,92,34,true,34,34,true,true,59,true]
