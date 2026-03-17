class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n=0
        for i in columnTitle:
            n=26*n+(ord(i)-64)
        return n