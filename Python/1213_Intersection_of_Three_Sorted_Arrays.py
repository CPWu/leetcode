# 2 Possible Solutions
# 1. Dictionary
# 2. 3 Pointers
class Solution:
    # Time: O(N), Space: O(N)
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Use python collections.counter library to count the frequencies of elements in all 3 arrays
        counter = collections.Counter(arr1 + arr2 + arr3)
        
        result = []
        for item in counter:
            if counter[item] == 3:
                result.append(item)
        return result