# 3 Possible Solutions
# 1. Sort Items
# 2. Heap
# 3. Quick Select

class Solution(object):
    # Time: O(NlogN), Space: O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]

    # Time: O(log k), Space: O(N log k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlargest method returns a list with n largets ements from the dataset.
        # [-1] is required to return the last element in the list
        return heapq.nlargest(k, nums)[-1]

    # Time: Avg(N)/Worst(N^2), Space: O(1)
    def findKthLargest(self, nums, k):
        k_index = len(nums) - k
        
        def quickSelect(leftPointer, rightPointer):
            # Chosing last element in array as pivotElement
            pivotElement = nums[rightPointer]
            # Start pointer at left most value
            pointer = leftPointer
            
            for i in range(leftPointer, rightPointer):
                if nums[i] <= pivotElement:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            
            nums[pointer], nums[rightPointer] = nums[rightPointer], nums[pointer]
            
            if pointer > k_index: return quickSelect(leftPointer, pointer - 1)
            elif pointer < k_index : return quickSelect(pointer + 1, rightPointer)
            else: return nums[pointer]
            
        return quickSelect(0, len(nums) - 1)