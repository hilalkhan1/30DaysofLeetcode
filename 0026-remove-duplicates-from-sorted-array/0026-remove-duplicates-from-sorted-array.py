class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = list(set(nums))
        l = len(set_nums)
        for i in range(l):
            nums[i] = set_nums[i]
        return len(set(nums))
        