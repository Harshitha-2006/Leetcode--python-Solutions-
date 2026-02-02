class Solution:
    def jump(self, nums: List[int]) -> int:
        j=0
        e,m=0,0
        for i in range(len(nums)-1):
            m=max(m,i+nums[i])
            if i==e:
                j+=1
                e=m
        return j