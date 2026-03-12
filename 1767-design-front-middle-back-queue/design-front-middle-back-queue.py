class FrontMiddleBackQueue:

    def __init__(self):
        self.q=deque()
 

    def pushFront(self, val: int) -> None:
        self.q.appendleft(val)
        

    def pushMiddle(self, val: int) -> None:
        n= len(self.q)//2
        self.q.insert(n, val)
        

    def pushBack(self, val: int) -> None:
        self.q.append(val)
        

    def popFront(self) -> int:
        if self.q: return self.q.popleft()
        else: return -1

        

    def popMiddle(self) -> int:
        if self.q: n=(len(self.q)-1)//2; val= self.q[n]; del self.q[n]; return val
        else: return -1

        

    def popBack(self) -> int:
        if self.q: return self.q.pop()
        else: return -1
        
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()