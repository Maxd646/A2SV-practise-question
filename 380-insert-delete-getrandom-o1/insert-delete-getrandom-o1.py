class RandomizedSet:

    def __init__(self):

        self.seen = {}
        self.arr = []

    def insert(self, val: int) -> bool:

        if val in self.seen:
            return False

        self.arr.append(val)
        j = len(self.arr)-1

        self.seen[val] = j

        return True
    

    def remove(self, val: int) -> bool:

        if val not in self.seen:
            return False
        
        indx = self.seen[val] 
        n = len(self.arr)

        self.arr[indx]= self.arr[n-1]

        if indx != n - 1:
            self.seen[self.arr[n - 1]] = indx

        
        self.arr.pop()

        del self.seen[val]

        return True

    def getRandom(self) -> int:

        return  random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()