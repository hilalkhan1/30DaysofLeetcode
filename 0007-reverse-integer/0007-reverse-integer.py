class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            a = int('-' + x[-1:0:-1])
            if a >= -2**(31) and a<= 2**(31)-1:
                return a
            else:
                return 0
        else:
            a = int(x[::-1])
            if a >= -2**(31) and a <= 2**(31) - 1:
                return a
            else:
                return 0
        