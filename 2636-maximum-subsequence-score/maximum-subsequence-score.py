from heapq import heappush,heappop
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int)->int:
        pairs=sorted(zip(nums1,nums2),key=lambda x:-x[1])
        h=[]
        s=0
        ans=0
        for num1,num2 in pairs:
            heappush(h,num1)
            s+=num1
            if len(h)>k:
                s-=heappop(h)
            if len(h)==k:
                ans=max(ans,s*num2)
        return ans
