class Solution:
    # Time: O(N), Space: O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        if len(nums) == 1:
            return []
        
        iterator = startNums = 0
        endNums = len(nums) - 1
        
        while iterator <= endNums:
            if nums[iterator] == 0:
                nums[iterator], nums[startNums] = nums[startNums], nums[iterator]
                iterator += 1
                startNums += 1
            elif nums[iterator] == 2:
                nums[iterator], nums[endNums] = nums[endNums], nums[iterator]
                endNums -= 1
            else:
                iterator += 1
        return nums