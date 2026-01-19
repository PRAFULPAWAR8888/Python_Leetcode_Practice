class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - 97] += 1

            key = tuple(freq)

            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
