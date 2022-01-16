class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        runningSum = 0
        lookup = {0: -1}
        
        for index, number in enumerate(nums):
            runningSum += number
            if k:
                runningSum %= k
            if runningSum in lookup:
                # Check if this remainder has been encountered before and of length 2
                if index - lookup[runningSum] > 1:
                    return True
            else:
                lookup[runningSum] = index
        return False