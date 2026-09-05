class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If the substring is empty, it is always a subsequence
        if not s:
            return True
            
        s_pointer = 0
        s_len = len(s)
        
        # Loop through the target string
        for char in t:
            # If characters match, move the pointer in 's'
            if char == s[s_pointer]:
                s_pointer += 1
                
            # If we matched all characters in 's', we are done
            if s_pointer == s_len:
                return True
                
        return False
