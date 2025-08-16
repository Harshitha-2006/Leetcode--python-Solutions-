class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ni={}
        for i,d in enumerate(nums):
            x=target-d
            if x in ni:
                return [ni[x],i]
            ni[d]=i
        