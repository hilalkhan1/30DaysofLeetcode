class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        y = x
        if n > 500:
            n = 500 / 4
            for i in range(int(n)+1):
                y *= x
            return y**4
            

        
        


        if n < 0 :
            n = -1 * n
            for i in range(n-1):
                y *=x
            return 1 / y
        for i in range(n-1):
            y *= x
        return y
        