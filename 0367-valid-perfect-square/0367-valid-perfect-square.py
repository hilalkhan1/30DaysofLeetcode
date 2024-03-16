class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left = 2
        right = num

        while left <= right:
            mid = left + (right - left)//2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
        