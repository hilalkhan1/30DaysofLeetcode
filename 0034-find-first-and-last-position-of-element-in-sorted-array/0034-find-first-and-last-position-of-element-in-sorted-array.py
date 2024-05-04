class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        start = -1
        while (left <= right):
            mid = (left + right) // 2
            if target <= nums[mid]:
                if target == nums[mid]:
                    start = mid
                right = mid - 1
            else:
                left = mid + 1
        left, right = 0, n-1
        end = -1

        while left <= right:
            mid = (left + right)//2
            if target >= nums[mid]:
                if target == nums[mid]:
                    end = mid
                left = mid + 1
            else:
                right = mid - 1

        return [start, end] 