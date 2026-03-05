class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)+1
        x=(n*(n-1))//2
        return x-sum(nums)