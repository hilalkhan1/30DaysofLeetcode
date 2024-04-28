class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0 or x == 1:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return self.myPow(1/x, -n)
        elif n % 4 == 0:
            return self.myPow(x*x*x*x, n//4)
        elif n % 3 == 0:
            return self.myPow(x*x*x, n//3)
        elif n % 2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return x * self.myPow(x, n - 1)

        
        

        