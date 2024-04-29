class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0 or n == 1:
            return s 

        longest = ""
        for i in range(n):
            sub = ""
            for j in range(i, n):
                sub = s[i:j+1]
                if sub[::-1] == sub and len(sub) > len(longest):
                    longest = sub
        return longest
        