class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output=0
        csum=0
        pre_sum={0:1}
        for n in nums:
            csum+=n
            diff=csum-k
            output+=pre_sum.get(diff,0)
            pre_sum[csum]=1+pre_sum.get(csum,0)
        return output