class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        
        for i in s:
            if i in map:
                if not stack or stack.pop() != map[i]:
                    return False
            
            else:
                stack.append(i)
        
        return not stack