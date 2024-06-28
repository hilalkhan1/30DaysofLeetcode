class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Ignore the leading WhiteSpaces
        s = s.lstrip()

        if len(s) == 0:
            return 0

        # Check for the sign
        sign = 1
        start = 0

        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        
        # Convert digits
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])

            # Handle the 32-bit signed integer range
            if sign * result > INT_MAX:
                return INT_MAX
            if sign * result < INT_MIN:
                return INT_MIN

        return sign * result