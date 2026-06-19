class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)

        # Manually clean: replace non-alpha chars with space
        cleaned = ""
        for ch in paragraph:
            if ch.isalpha():
                cleaned += ch.lower()
            else:
                cleaned += " "

        words = cleaned.split()

        # Count manually
        freq = {}
        for word in words:
            if word not in banned_set:
                freq[word] = freq.get(word, 0) + 1

        # Find max
        return max(freq, key=freq.get)