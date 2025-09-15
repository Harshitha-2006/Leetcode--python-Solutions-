from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2) or set(word1)!=set(word2):
            return False
        f1=Counter(word1)
        f2=Counter(word2)
        if sorted(f1.values())!=sorted(f2.values()):
            return False
        return True
        