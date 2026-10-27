class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[i],nums[pos]=nums[pos],nums[i]
                pos+=1