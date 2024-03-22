class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for letter in s:
            if letter in s_count.keys():
                s_count[letter] += 1
            else:
                s_count[letter] = 1
        
        for letter in t:
            if letter in t_count.keys():
                t_count[letter] += 1
            else:
                t_count[letter] = 1
        return s_count == t_count

        