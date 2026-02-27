class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pre,res=0,[]
        for i in range(len(s)+1):
            if i and not Counter(s[pre:i]) & Counter(s[i:]):
                res.append(i-pre)
                pre=i
        return res

        