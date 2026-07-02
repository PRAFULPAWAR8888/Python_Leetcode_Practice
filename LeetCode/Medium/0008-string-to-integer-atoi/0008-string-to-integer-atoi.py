class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0 
        n = len(s)
        INT_MIN , INT_MAX = -2**31 , 2**31 - 1

        #1. Skip leading whitespace

        while i < n and s[i]  == ' ':
            i += 1

        if i == n:
            return 0
        

        #2. Handle optional sign
        sign = 1
        if s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            
            i += 1

        #3 Read digits
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num *= sign

        #4 Clamp to 32- bit signed range

        if num < INT_MIN:
            return INT_MIN
        
        if num > INT_MAX:
            return INT_MAX
        
        return num
        