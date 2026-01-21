class Solution:
    def tribonacci(self, n: int) -> int:
        memo={0:0,1:1,2:1}
        def r(n):
            if n not in memo:
                memo[n]=r(n-1)+r(n-2)+r(n-3)
            return memo[n]
        return r(n)
