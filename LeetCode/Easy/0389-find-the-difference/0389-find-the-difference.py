class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lst = list(s)

        for ch in t:
            if ch in lst:
                lst.remove(ch)
            else:
                return ch       