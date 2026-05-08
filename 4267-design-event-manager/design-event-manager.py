import heapq
class EventManager:
    def __init__(self, events: list[list[int]]):
        self.heap=[[-pre, val] for val, pre in events]
        heapq.heapify(self.heap)
        self.hash = {val: pre for val, pre in events}
        return
    
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        if eventId in self.hash:
            self.hash[eventId] = newPriority
        heapq.heappush(self.heap, [-newPriority, eventId])
        
    def pollHighest(self) -> int:
        while self.heap:
            pre, val = heapq.heappop(self.heap)
            pre = - pre
            # print(self.hash)
            # print(pre, val)
            if val in self.hash and self.hash[val] == pre:
                self.hash[val] = float("inf")
                return val
        return -1
        
# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()