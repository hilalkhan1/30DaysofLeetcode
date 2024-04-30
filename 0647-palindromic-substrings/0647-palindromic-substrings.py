class Solution:
    def countSubstrings(self, s: str) -> int:
        subs = []
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    subs.append(sub)
        return len(subs)
        