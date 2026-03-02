class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for ch in s:
            if ch.isalnum(): # keep only letters & numbes
                cleaned += ch.lower()
        return cleaned == cleaned[::-1]

        