from math import log10
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b == 0:
            return a
        # Mask to detect overflow
        mask = 0xffffffff

        while b != 0:
            # Perfom addition without considering carry
            sum_without_carry = (a ^ b) & mask

            # Calculate carry
            carry = ((a & b) << 1) & mask

            # Update values of a and b for the next iteration
            a = sum_without_carry
            b = carry

        # Handle negative overflow
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a