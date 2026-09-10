class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # 1. Adjust for 1-based indexing
            columnNumber -= 1
            
            # 2. Get the remainder to find the current character
            remainder = columnNumber % 26
            
            # 3. Convert remainder to its ASCII character ('A' is 65)
            char = chr(remainder + ord('A'))
            result.append(char)
            
            # 4. Move to the next positional column digit
            columnNumber //= 26
            
        # Since we gathered characters from right to left, reverse the result
        return "".join(reversed(result))
