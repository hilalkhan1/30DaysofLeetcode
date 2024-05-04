class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # output = []

        # if n == 0:
        #     return [-1, -1]
        # for i in range(n):
        #     if nums[i] == target and len(output)<2:
        #         output.append(i)
        #         continue
        #     if nums[i] == target and len(output) >= 2:
        #         output.pop()
        #         output.append(i)
        # if len(output) == 0:
        #     return [-1, -1]
        # if len(output) == 1:
        #     output.append(output[0])
        #     return output

        # return output

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



        