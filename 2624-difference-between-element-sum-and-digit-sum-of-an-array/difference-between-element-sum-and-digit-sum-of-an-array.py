class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        d1=sum(nums)
        x=[]
        for i in range(len(nums)):
            n=nums[i]
            if n>=1 or n<9:
                x.append(n)
            if n>=10:
                j=n
                d=0
                while j>0:
                    d=j%10
                    x.append(d)
                    j=j//10
        for i in x:
            if i>=10:
                x.remove(i)
        d2=sum(x)
        return abs(d1-d2)