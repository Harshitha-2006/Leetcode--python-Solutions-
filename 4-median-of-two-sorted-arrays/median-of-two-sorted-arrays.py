import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1+nums2
        r=np.median(l)
        return r

