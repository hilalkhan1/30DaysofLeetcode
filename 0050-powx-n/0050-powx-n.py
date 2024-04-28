class Solution:
    def myPow(self, x: float, n: int) -> float:

        def my_func(x, n):
            if n == 0: 
                return 1
            result = my_func(x*x, n//2)
            return result * x if n&1 else result
        return my_func(x, n) if n>0 else 1 / my_func(x, -n)
        
        

        