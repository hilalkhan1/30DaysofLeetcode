class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rev_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            rev_nums[i] *= rev_nums[i - 1] or 1
        return max(nums + rev_nums)

        