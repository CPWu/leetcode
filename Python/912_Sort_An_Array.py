# Possible Solutions
# 1. Merge Sort
# 2. Quicksort
# 3. Insertion Sort
# 4. Selection Sort
# 5. Bubble Sort
# 6. Heapsort
# 7. Radix Sort
# 8. Counting Sort

class Solution:

    # Time: O(NlogN), Space: O(N) 
    def sortArray(self, nums: List[int]) -> List[int]:
        # Empty List or Single Element List
        if len(nums) <= 1:
            return nums
        
        # Middle index of input list
        middleIndex = len(nums) // 2
        
        # Left/Right sub-arrays
        leftSubArray = nums[:middleIndex]
        rightSubArray= nums[middleIndex:]
        
        return self.mergeSortHelper(self.sortArray(leftSubArray), self.sortArray(rightSubArray))
    
    def mergeSortHelper(self, leftSubArray: List[int], rightSubArray: List[int]) -> List[int]:
        # Initialize an Empty Array Equal to Size of Left + Right Sub-Array
        result = [None] * (len(leftSubArray) + len(rightSubArray))
        
        # Initialize indexes to keep track of where we are in the three arrays
        i = j = k = 0
        
        while i < len(leftSubArray) and j < len(rightSubArray):
            if leftSubArray[i] <= rightSubArray[j]:
                result[k] = leftSubArray[i]
                i += 1
            else:
                result[k] = rightSubArray[j]
                j += 1
            k += 1
        
        while i < len(leftSubArray):
            result[k] = leftSubArray[i]
            k += 1
            i += 1
            
        while j < len(rightSubArray):
            result[k] = rightSubArray[j]
            k += 1
            j += 1
            
        return result
        