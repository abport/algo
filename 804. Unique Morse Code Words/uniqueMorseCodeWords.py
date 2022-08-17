# Complexity ---------------------------------------------------------------------
# Time Complexity: O(S)O(S), where SS is the sum of the lengths of words in words. 
#                  We iterate through each character of each word in words.
# Space Complexity: O(S)O(S).
# --------------------------------------------------------------------------------

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = []
        
        for word in words:
            morse = ""
            for ch in word:
                morse += morseCode[ord(ch) - 97]
            if morse not in res:
                res.append(morse)
        
        return len(res)
        

# Second Method (Solution from LeetCode)
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)