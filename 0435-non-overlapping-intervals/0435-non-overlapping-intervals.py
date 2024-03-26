class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals by second element
        intervals.sort(key=lambda x:x[1])
        n = len(intervals)
        previous = 0
        ans = 0

        for i in range(1, n):
            current_s, current_e = intervals[i]
            previous_s, previous_e = intervals[previous]

            if (current_s < previous_e):
                ans += 1

                if (current_e <= previous_e):
                    previous = i
            
            else:
                previous = i

        return ans




        