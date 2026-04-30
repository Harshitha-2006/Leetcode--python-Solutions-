class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        l=len(pref)
        for i in words:
            if len(i)>=l and i[:l]==pref:
                c+=1
        return c