
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not str:
            return ""


        

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix

               
       
