class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s) 
        left = 0
        right = n - 1

        for i in range(n):
            if left < right:
                s[left],s[right] = s[right], s[left]
                left += 1
                right -= 1
        return None




        

       


        
        