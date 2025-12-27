class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()      # removes extra spaces automatically
        words.reverse()       # reverse word order
        return " ".join(words)
