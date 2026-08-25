class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        dict1={}
        if k not in nums:
            return k
        n=len(nums)
        count=1
        for i in range(n):
            if nums[i] % k ==0:
                dict1[count]=nums[i]
                count+=1

        multiple =k
        while multiple  in dict1.values():
            multiple+=k

        return multiple