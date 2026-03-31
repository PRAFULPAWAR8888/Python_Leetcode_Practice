class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#'+'#'.join(s)+'#'
        n = len(t)
        p = [0]* n
        center = right = 0

        for i in range(n):
            mirror = 2* center - i

            if i < right:
                p[i] = min(right - i, p[mirror])
            
            lo, hi = i - p[i] - 1, i + p[i] + 1
            while lo >= 0 and hi < n and t[lo] == t[hi]:
                p[i] += 1
                lo -= 1
                hi += 1

            
            if i + p[i] > right :
                center = i + p[i]
        
        max_len, best_center = max((v,i) for i, v in enumerate(p))

        start = (best_center - max_len) // 2
        return s[start: start + max_len]



        
        