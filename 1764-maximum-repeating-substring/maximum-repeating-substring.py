class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        c=0
        t=word
        for i in sequence:
            if t in sequence:
                c+=1
                t+=word
            else:
                break
        return c