class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest=0
        set1=set(nums)
        for num in set1:
            if num -1 not in set1:
                current = num 
                length=1

                while current + 1 in set1:
                    current +=1
                    length+=1
                longest  = max(length, longest)
        return longest            
        