class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]

        for char in operations:
            if char == "C":
                stack.pop()
            elif char == "D":
                double=stack[-1]*2
                stack.append(double)
            elif char == "+":
                add=stack[-1]+stack[-2]
                stack.append(add)
            else:
                stack.append(int(char))

        return sum(stack)                
