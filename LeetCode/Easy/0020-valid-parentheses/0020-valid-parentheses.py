class Solution:
    def isValid(self, s: str) -> bool:
        if ((len(s))%2) != 0:
            return False
        q = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                q.append(s[i])
            else:
                if len(q) !=0:
                    popped = q.pop(-1)
                else:
                    return False
                if popped=='(':
                    if s[i]==')':
                        pass
                    else:
                        return False
                if popped=='[':
                    if s[i]==']':
                        pass
                    else:
                        return False
                if popped=='{':
                    if s[i]=='}':
                        pass
                    else:
                        return False
        if len(q) == 0:
            return True
        else:
            return False
        