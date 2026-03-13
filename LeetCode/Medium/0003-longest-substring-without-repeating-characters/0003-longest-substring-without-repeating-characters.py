class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0

        seen = []
        max_len = 0

        while right < len(s):
            if s[right] not in seen:
                seen.append(s[right])
                right += 1
                max_len = max(max_len, right - left)

            else:
                seen.remove(s[left])
                left += 1
        return max_len      



           


            





        

    
        