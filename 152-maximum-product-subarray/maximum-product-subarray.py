class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx=mn=m=nums[0]
        for i in nums[1:]:
            mx,mn=max(i,mx*i,mn*i),min(i,mx*i,mn*i)
            m=max(m,mx)
        return m