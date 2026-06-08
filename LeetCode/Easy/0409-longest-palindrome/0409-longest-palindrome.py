class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        counts = Counter(s)
        length = 0
        has_odd = False

        for count in counts.values():
            length += count if count % 2 == 0 else count - 1
            if count % 2 != 0:
                has_odd = True
        
        return length + (1 if has_odd else 0 )

        