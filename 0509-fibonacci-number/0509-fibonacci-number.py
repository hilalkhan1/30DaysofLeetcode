class Solution:
    def fib(self, n: int) -> int:
        f = [0] * (n+2)

        f[0] = 0
        f[1] = 1

        for i in range(2, n+1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]





        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
        