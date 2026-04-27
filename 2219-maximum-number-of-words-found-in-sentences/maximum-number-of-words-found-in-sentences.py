class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=0
        m=0
        for i in sentences:
            c=len(i.split())
            m=max(m,c)
        return m