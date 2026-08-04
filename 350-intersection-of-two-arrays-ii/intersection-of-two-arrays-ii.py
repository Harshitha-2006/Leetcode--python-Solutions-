from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        l=s1.intersection(s2)
        res=[]
        c1=Counter(nums1)
        c2=Counter(nums2)
        for i in l:
            res.extend([i]*min(c1[i],c2[i]))
        return res