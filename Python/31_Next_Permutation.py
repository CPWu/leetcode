class Solution(object):
    # Time: O(N), Space: (1)    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Find first decreasing element starting from the right.
        # Find number just larger than the previously chosen number on the left.
        # Swap the Elements
        # Reverse the numbers prior to the pivot.

        length = len(nums)
        pivot = 0
        for i in range(len(length)-1, 0, -1): # Reverse Order
            if nums[i-1] < nums[i]:
                pivot = i
                break
        # If pivot is 0 that means its maximized so just sort array and return (lowest possible number)
        if pivot == 0:
            nums.sort()
            return

        swap = length - 1

        # Find number just larger than the previously chosen number on the left.
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1
    
        # Swap the Elements
        nums[swap], nums[pivot-1] = nums[pivot - 1], nums[swap]
        
        # Reverse the numbers prior to the pivot.
        nums[pivot:] = sorted(nums[pivot:])
