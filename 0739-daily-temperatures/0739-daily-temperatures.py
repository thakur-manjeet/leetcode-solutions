class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]

        for i in range(n):
            curr_temperature=temperatures[i]

            while st and curr_temperature > temperatures[st[-1]]:
                pop_idx=st.pop()
                ans[pop_idx]=i-pop_idx
            st.append(i)          

        return ans