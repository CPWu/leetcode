# 4 Possible Solutions
# 1. Recursion
# 2. Top-Down Memoization
# 3. Bottom-Up Tabulation Iterative
# 4. Bottom-Up Iterative

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

    # Time: O(N), Space: O(N)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        # Initialize an empty cache of size N
        cache = [0] * (n + 1)
        
        cache[1] = 1
        
        # Loop through values in n starting at 3rd index
        for i in range(2, n + 1):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[n]

    # Time: O(N), Space: O(1)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        current = 0
        prev1 = 1
        prev2 = 0
        
        for i in range(2, n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return current