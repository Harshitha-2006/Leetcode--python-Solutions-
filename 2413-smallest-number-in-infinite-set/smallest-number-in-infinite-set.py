class SmallestInfiniteSet:

    def __init__(self):
        self.h=[]
        self.m=1

    def popSmallest(self) -> int:
        if self.h:
            return heapq.heappop(self.h)
        self.m+=1
        return self.m-1

    def addBack(self, num: int) -> None:
        if self.m>num and num not in self.h:
            heapq.heappush(self.h,num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)