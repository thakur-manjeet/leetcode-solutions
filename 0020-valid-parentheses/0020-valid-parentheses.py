class Solution:
    def isValid(self, s: str) -> bool:
        mapp={")": "(", "]": "[", "}": "{"}
        stack=[]

        for char in s:
            if char in mapp:
                if stack:
                    top=stack.pop()
                else:
                    top="#"

                if mapp[char]!=top:
                    return False    
            else:
                stack.append(char)
        return len(stack) == 0