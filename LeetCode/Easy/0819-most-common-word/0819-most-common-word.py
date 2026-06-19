from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        paragraph = paragraph.lower()

        # replace punctuation with space
        paragraph = re.sub(r"[^\w\s]", " ", paragraph)

        words = paragraph.split()

        banned = set(banned)

        filtered_words = []

        for word in words:
            if word not in banned:
                filtered_words.append(word)

        frequency = Counter(filtered_words)

        return frequency.most_common(1)[0][0]