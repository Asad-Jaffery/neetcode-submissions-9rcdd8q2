class Solution:

    cache = {}

    def climbStairs(self, n: int) -> int:

        if n in self.cache:
            return self.cache[n]

        if n == 1:
            value = 1
            self.cache[n] = value
            return value
        elif n == 2:
            value = 2
            self.cache[n] = value
            return value
        else: 
            value = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.cache[n] = value
            return value
        