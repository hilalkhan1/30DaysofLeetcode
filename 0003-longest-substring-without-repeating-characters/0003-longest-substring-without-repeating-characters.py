class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dic = dict()
        l, r = 0, 0
        length = 0

        while (r < n):
            if s[r] in dic.keys():
                l = max(dic[s[r]] + 1, l)
            
            dic[s[r]] = r

            length = max(length, r - l + 1)

            r += 1

        return length








        