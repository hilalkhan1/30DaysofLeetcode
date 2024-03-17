class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for num in nums:
            # if nums.count(num) >= 2:
                # return True
        # return False
        return len(nums) != len(set(nums))
        