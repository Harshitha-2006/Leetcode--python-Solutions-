class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set=set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            if dp[i]:
                for w in word_set:
                    if s[i:i+len(w)]==w:
                        dp[i+len(w)]=True
        return dp[-1]
