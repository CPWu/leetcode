# Time: O(log N), Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer <= rightPointer:
            midPointer = (leftPointer + rightPointer) // 2
            if nums[midPointer] == target:
                return midPointer
            elif nums[midPointer] < target:
                leftPointer = midPointer + 1
            else:
                rightPointer = midPointer - 1
        return -1