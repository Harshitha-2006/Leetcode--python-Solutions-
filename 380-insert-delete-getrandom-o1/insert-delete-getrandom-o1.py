class RandomizedSet:

    def __init__(self):
        self.s={}
        self.m={}
        self.c=0
        
    def insert(self, val: int) -> bool:
        b=val in self.s
        if not b:
            self.s[val]=self.c
            self.m[self.c]=val
            self.c+=1
        return not b

    def remove(self, val: int) -> bool:
        b=val in self.s
        if b:
            index=self.s[val]
            del self.s[val]
            self.c-=1
            x=self.m[self.c]
            del self.m[self.c]
            if val!=x:
                self.m[index]=x
                self.s[x]=index
        return b


    def getRandom(self) -> int:
        return self.m[random.randint(0,self.c-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()