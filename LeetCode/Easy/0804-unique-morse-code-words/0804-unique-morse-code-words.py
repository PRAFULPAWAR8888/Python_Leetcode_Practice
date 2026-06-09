class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
            morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
             ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
             "...","-","..-","...-",".--","-..-","-.--","--.."]

            transformations = set()

            for word in words:
                code = ""
                for c in word:
                    index = ord(c) - ord("a") #get alphabets postion
                    code += morse[index] # add its morse code
                transformations.add(code)
            
            return len(transformations)
        