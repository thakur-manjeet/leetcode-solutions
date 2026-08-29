class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:      
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        sorted_items=sorted(dict1.items(),key=lambda item:item[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans                