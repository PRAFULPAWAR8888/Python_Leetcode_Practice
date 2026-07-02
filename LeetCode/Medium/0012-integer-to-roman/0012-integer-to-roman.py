class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        
        # Process each place value: thousands, hundreds, tens, ones
        digits = [1000, 100, 10, 1]
        result = ""
        
        for base in digits:
            digit = (num // base) % 10
            
            if digit <= 3:
                # e.g., 1, 2, 3 -> I, II, III
                result += roman_map[base] * digit
            elif digit == 4:
                # e.g., 4 -> IV, 40 -> XL
                result += roman_map[base] + roman_map[base * 5]
            elif digit <= 8:
                # e.g., 5,6,7,8 -> V, VI, VII, VIII
                result += roman_map[base * 5] + roman_map[base] * (digit - 5)
            else:  # digit == 9
                # e.g., 9 -> IX, 90 -> XC
                result += roman_map[base] + roman_map[base * 10]
        
        return result
        