class MinStack:

    def __init__(self):
        self.st=[]
        self.min_st=[]

    def push(self, val: int) -> None:
        self.st.append(val)

        if not self.min_st:
            self.min_st.append(val)
        else:
            self.min_st.append(min(val,self.min_st[-1]))

        

    def pop(self) -> None:
        if not self.st:
            return -1
        self.min_st.pop()
        return self.st.pop()
    def top(self) -> int:
        if not self.st:
            return -1
        return self.st[-1]

    def getMin(self) -> int:
        if not self.min_st:
            return -1
        return self.min_st[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()