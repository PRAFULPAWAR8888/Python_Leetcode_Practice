class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")

        v_freq = {}
        c_freq = {}

        for ch in s:
            if ch in vowels:
                v_freq[ch] = v_freq.get(ch, 0) + 1
            else:
                c_freq[ch] = c_freq.get(ch, 0) + 1

        max_v = max(v_freq.values()) if v_freq else 0
        max_c = max(c_freq.values()) if c_freq else 0

        return max_v + max_c
        