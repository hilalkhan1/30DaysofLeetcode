class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):
            s, e = intervals[i]
            if s > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif e < newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
            
        ans.append(newInterval)
        return ans

