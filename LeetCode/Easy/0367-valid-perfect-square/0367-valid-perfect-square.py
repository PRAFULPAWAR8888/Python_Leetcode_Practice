class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = int(math.isqrt(num))
        return root * root == num

            