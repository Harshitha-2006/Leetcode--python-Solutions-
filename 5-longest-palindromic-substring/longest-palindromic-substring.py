class Solution:
    def longestPalindrome(self, s):
        l = ''
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            l = s[i]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1] is True:
                        dp[i][j] = True
                        if len(l) < len(s[i:j + 1]):
                            l = s[i:j + 1]
        return l
