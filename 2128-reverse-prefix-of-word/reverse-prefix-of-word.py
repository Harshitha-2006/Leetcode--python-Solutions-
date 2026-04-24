class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        r=""
        c=0
        if ch not in word:
            return word
        for i in word:
            if i==ch:
                r+=i
                c+=1
                break
            r+=i
            c+=1
        x=""
        for i in reversed(r):
            x+=i
        for i in range(c,len(word)):
            x+=word[i]
        return x