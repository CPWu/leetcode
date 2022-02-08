# 4 Possible Solutions
# 1. Cheat using .reverse()
# 2. Slicing
# 3. Recursion, In-Place
# 4. Two Pointers

# Time: O(N), Space: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        return s.reverse()

# Time: O(N), Space: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        return s

# Time: O(N), Space: O(N)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(leftPonter, rightPointer):
            if leftPonter < rightPointer:
                s[leftPonter], s[rightPointer] = s[rightPointer], s[leftPonter]
                helper(leftPonter + 1, rightPointer - 1)
                
        helper(0, len(s) - 1)

# Time: O(N), Space: O(1)
class Solution:
    def reverseString(self, s):
        leftPointer, rightPointer = 0, len(s) - 1
        
        while leftPointer < rightPointer:
            s[leftPointer], s[rightPointer]= s[rightPointer], s[leftPointer]
            leftPointer += 1
            rightPointer -= 1