class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        output = []

        if n == 0:
            return [-1, -1]
        for i in range(n):
            if nums[i] == target and len(output)<2:
                output.append(i)
                continue
            if nums[i] == target and len(output) >= 2:
                output.pop()
                output.append(i)
        if len(output) == 0:
            return [-1, -1]
        if len(output) == 1:
            output.append(output[0])
            return output

        return output

        