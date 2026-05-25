class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        arr = []
        for i in letters:
            if ord(target) < ord(i):
                arr.append(ord(i))
        
        if arr:
            return chr(min(arr))
        
        else:
            return letters[0]