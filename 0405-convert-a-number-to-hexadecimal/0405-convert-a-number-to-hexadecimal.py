class Solution:
    def toHex(self, num: int) -> str:
        # Edge case: if the number is zero, return "0" immediately
        if num == 0:
            return "0"
            
        # Hexadecimal character mapping
        hex_map = "0123456789abcdef"
        
        # Handle negative numbers using Two's Complement.
        # Masking with 0xFFFFFFFF constrains the number to a 32-bit unsigned integer.
        if num < 0:
            num &= 0xFFFFFFFF
            
        result = []
        while num > 0:
            remainder = num & 15
            result.append(hex_map[remainder])
            
            num >>= 4

        return "".join(reversed(result))
