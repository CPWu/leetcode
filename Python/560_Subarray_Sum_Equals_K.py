from collections import defaultdict


class Solution(object):
    # # Time:O(N), SpaceO(N)
    # def subarraySum(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     result = 0
    #     currentSum = 0
    #     prefixSums = {0:1}
        
    #     for n in nums:
    #         currentSum += n
    #         difference = currentSum - k
            
    #         result += prefixSums.get(difference, 0)
    #         prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)
        
    #     return result

    # Time: O(N), Space: O(N)
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        currentSum = 0
        prefixSums = defaultdict(int)

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum == k:
                result += 1
            if currentSum - k in prefixSums:
                result += prefixSums[currentSum-k]
            
            prefixSums[currentSum-1]
        return result
