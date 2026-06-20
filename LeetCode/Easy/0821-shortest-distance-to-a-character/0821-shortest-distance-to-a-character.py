class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        result = [float('inf')] * n

        # Left pass: scan left to right
        prev = float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = abs(i - prev)

        # Right pass: scan right to left
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], abs(i - prev))

        return result
        
        
                
        