class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        for i in range(len(s)):
            if len(x) == 0:
                x.append(s[i])
            elif (s[i] == ")" and x[-1] == "(") or (s[i] == "}" and x[-1] == "{") or (s[i] == "]" and x[-1] == "["):
                x.pop()
            else:
                x.append(s[i])
        return len(x) == 0
        