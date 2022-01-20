class Solution:
#     # Time: O(N), Space: O(1)
#     def isAnagram(self, s: str, t: str) -> bool:
        
#         # Takes care of either string being empty.
#         if len(s) != len(t):
#             return False

#         sDict = Counter(s)
        
#         for character in t:
#             sDict[character] -= 1
#             if sDict[character] < 0:
#                 return False
#         return True

    # # Time: O(NlogN), Space: O(1)
    # # .sort modifies the existing list, sorted() creates new list
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)

    # Time: O(N), Space: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)