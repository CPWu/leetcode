class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Two Possible Solutions
        # Time: O(N), Space: O(N)
        sortedSquares = [0 for _ in nums]
        leftPointer = 0
        rightPointer = len(nums)-1
        
        for index in reversed(range(len(nums))):
            leftPointerSquare = nums[leftPointer] * nums[leftPointer]
            rightPointerSquare = nums[rightPointer] * nums[rightPointer]
            
            if abs(leftPointerSquare) > abs(rightPointerSquare):
                sortedSquares[index] = leftPointerSquare
                leftPointer += 1
            else:
                sortedSquares[index] = rightPointerSquare
                rightPointer -= 1
        
        return sortedSquares

    # # Time: O(NlogN), Space: O(N)
    # def sortedSquares(self, nums):
    #     sortedSquares = [0 for _ in nums]

    #     for index in range(len(nums)):
    #         value = nums[index]
    #         sortedSquares[index] = value * value

    #     sortedSquares.sort()

    #     return sortedSquares

nums = [-4,-1,0,3,10]
[0,1,9,16,100]
soln = Solution()
print(soln.sortedSquares(nums))