# 4 Possible Solutions
# 1. Recursion
# 2. Memoization
# 3. Bottom-Up Tabulation Iterative
# 4. Two Pointers

class Solution:
    #: Time: (2^n), Space: O(N)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib(n - 1) + self.fib(n - 2)

    # Time: O(N), Space: O(N)
    cache = {0: 0, 1: 1}
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.cache[n]