class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or len(strs) == 1:
            return [strs]

        d = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            d[key].append(word)
        return d.values()
        
        