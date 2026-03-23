class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ["a","e","i","o","u","A","E","I","O","U"]

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] not in v:
                   left += 1

            elif s[right] not in v:
                 right -= 1

            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)
        