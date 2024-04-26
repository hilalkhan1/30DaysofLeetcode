class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left_pointer = 0
        max_frequency = 0

        for index in range(len(s)):
            count[s[index]] = 1 + count.get(s[index], 0)
            max_frequency = max(max_frequency, count[s[index]])

            if (index - left_pointer + 1) - max_frequency > k:
                count[s[left_pointer]] -= 1
                left_pointer += 1

            result = max(max_frequency, index - left_pointer + 1)
        return result





        