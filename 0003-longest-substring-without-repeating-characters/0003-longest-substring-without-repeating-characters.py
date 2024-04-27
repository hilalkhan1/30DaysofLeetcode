class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        n = len(s)
        for i in range(n):
            sub = ""
            for j in range(i, n):
                if s[j] in sub:
                    break
                else:
                    print(i)
                    sub += s[j]
            if len(sub) > len(string):
                string = sub
        return len(string)







        