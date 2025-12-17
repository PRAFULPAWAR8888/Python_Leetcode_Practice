class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        step1 = 1
        step2 = 2

        for _ in range(3, n + 1):
            curr = step2 + step1
            step1 = step2
            step2 = curr
        
        return step2
