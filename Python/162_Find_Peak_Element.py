class Solution(object):
    # Time: O(LogN), Space: O(1)
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer < rightPointer:
            middle = (leftPointer + rightPointer) // 2
            if nums[middle] < nums[middle + 1]:
                leftPointer = middle + 1
            else:
                rightPointer = middle

        return leftPointer