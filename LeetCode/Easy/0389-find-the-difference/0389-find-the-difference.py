class Solution:
    def my_ord(self, ch):
        letters = "abcdefghijklmnopqrstuvwxyz"

        for i in range(26):
            if letters[i] == ch:
                return i + 97

    def my_chr(self, num):
        letters = "abcdefghijklmnopqrstuvwxyz"
        return letters[num - 97]

    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for c in s + t:
            result ^= self.my_ord(c)

        return self.my_chr(result)