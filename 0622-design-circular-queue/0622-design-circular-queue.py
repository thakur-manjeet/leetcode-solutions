class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.arr = [None] * self.cap
        self.f = 0
        self.r = -1
        self.curr_size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        # Circular increment of rear pointer
        self.r = (self.r + 1) % self.cap
        self.arr[self.r] = value
        self.curr_size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        # Circular increment of front pointer
        self.f = (self.f + 1) % self.cap
        self.curr_size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.f]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.r]

    def isEmpty(self) -> bool:
        return self.curr_size == 0

    def isFull(self) -> bool:
        return self.curr_size == self.cap
    


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()