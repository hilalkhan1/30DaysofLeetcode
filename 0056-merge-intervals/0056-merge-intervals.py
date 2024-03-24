class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)
        intervals.sort()
        ans = []
        for i in range(n):
            start, end = intervals[i]
            if len(ans) == 0 or start > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], end)
                  

        return ans