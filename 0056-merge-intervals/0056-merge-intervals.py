class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans=[intervals[0]]
        pos=0
        for i in range(1,n):
            if ans[pos][1] >= intervals[i][0]:

                ans[pos][1] = max(ans[pos][1],intervals[i][1])
            else:
                ans.append(intervals[i])
                pos += 1
        return ans