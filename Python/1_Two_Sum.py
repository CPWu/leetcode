class Solution(object):
    # There are three possible solutions depending on the trade-offs:

    # # Time: O(N^2), Space: O(1)
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     for i in range(len(nums)-1):
    #         firstNum = nums[i]
    #         for j in range(i + 1, len(nums)):
    #             secondNum = nums[j]
    #             if firstNum + secondNum == target:
    #                 return [i, j]
        # return []

    # # Time: O(N), Space: O(N)    
    # def twoSum(self, nums, target):
    #     auxSpace = {}

    #     for index, value in enumerate(nums):
    #         potentialValue = target - value
    #         if potentialValue in auxSpace:
    #             return [auxSpace[potentialValue], index]
    #         else:
    #             auxSpace[value] = index
    #     return []

    # Time: O(NlogN), Space: O(1)
    def twoSum(self, nums, target):
        nums.sort()
        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer < rightPointer:
            currentSum = nums[leftPointer] + nums[rightPointer]
            if currentSum == target:
                return [leftPointer, rightPointer]
            if currentSum < target:
                leftPointer += 1
            if currentSum > target:
                rightPointer -= 1
        
        return []


nums = [2, 7, 11, 15]
target = 9
soln = Solution()
print(soln.twoSum(nums, target))