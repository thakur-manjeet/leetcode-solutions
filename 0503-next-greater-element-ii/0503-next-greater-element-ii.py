class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        stack=[]

        for i in range(2 * n):
            curr= nums[i %n]
            while stack and curr> nums[stack[-1]]:
                pop_idx=stack.pop()
                ans[pop_idx]=curr

            if i < n:
                stack.append(i)

        return ans            