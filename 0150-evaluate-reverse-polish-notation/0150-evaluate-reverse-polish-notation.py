class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for token in tokens:
            if token =="+":
                right=st.pop()
                left=st.pop()
                st.append(left+right)
            elif token == "-":
                right=st.pop()
                left=st.pop()
                st.append(left-right)
            elif  token== "*":
                right=st.pop()
                left=st.pop()
                st.append(left*right)
            elif token == "/":
                right=st.pop()
                left=st.pop()
                st.append(int(left/right)) 

            else:
                st.append(int(token))

        return st[-1]                   