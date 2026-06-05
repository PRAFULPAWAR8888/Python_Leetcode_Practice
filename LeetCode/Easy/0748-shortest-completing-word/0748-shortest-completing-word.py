class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        plate_count = Counter(c.lower() for c in licensePlate if c.isalpha())

        result = None
        for word in words:
            word_count = Counter(word.lower())

            if all(word_count[ch] >= freq for ch, freq in plate_count.items()):

                if result is None or len(word) < len(result):
                    result = word
        
        return result

        