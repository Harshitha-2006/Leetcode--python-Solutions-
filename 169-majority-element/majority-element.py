class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        l=len(nums)
        return nums[l//2]