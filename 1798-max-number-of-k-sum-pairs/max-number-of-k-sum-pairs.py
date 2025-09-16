class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d=defaultdict(list)
        c=0
        for i,n in enumerate(nums):
            x=k-n
            if d[x]:
                c+=1
                d[x].pop()
            else:
                d[n].append(i)
        return c

        