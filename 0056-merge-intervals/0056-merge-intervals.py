class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)
        intervals.sort()
        ans = []
        for i in range(n):
            start, end = intervals[i]
            if (len(ans) != 0) and end <= ans[-1][1]:
                continue
            for j in range(n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break
            ans.append([start, end])
                  

        return ans