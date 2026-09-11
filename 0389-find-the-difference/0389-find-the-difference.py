class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        char_xor = 0
        
        for char in s:
            char_xor ^= ord(char)
            
        for char in t:
            char_xor ^= ord(char)
        
        return chr(char_xor)
