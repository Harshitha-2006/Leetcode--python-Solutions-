from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=Counter(arr)
        l=[]
        for i in d:
            if d[i]==1:
                l.append(i)
        if len(l)<k:
            return ""
        else:
            return l[k-1]