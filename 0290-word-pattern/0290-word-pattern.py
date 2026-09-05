class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string s into individual words
        words = s.split()
        
        # If the number of characters in pattern doesn't match the number of words, it's invalid
        if len(pattern) != len(words):
            return False
            
        # Two dictionaries to ensure a 1-to-1 (bijection) mapping
        char_to_word = {}
        word_to_char = {}
        
        # Use zip to loop through both sequences simultaneously in order
        for char, word in zip(pattern, words):
            # Check character to word mapping
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
                
            # Check word to character mapping
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
                
        return True
