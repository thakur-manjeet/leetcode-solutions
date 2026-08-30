class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        answer={}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller=stack.pop()
                answer[smaller]=num
            stack.append(num)
        while stack:
            popped_num = stack.pop()
            answer[popped_num] = -1

        ans=[]
        for num in nums1:
            ans.append(answer[num])
            
        return ans
