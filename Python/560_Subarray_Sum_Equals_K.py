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
        prevSum = defaultdict(int)
        
        result = 0
        
        currentSum = 0
        
        for i in range(0,len(nums)):
            currentSum += nums[i]
            
            if currentSum == k:
                result += 1
            
            if currentSum - k in prevSum:
                result += prevSum[currentSum - k]
            
            prevSum[currentSum] += 1       
        return result

         def continuousSum(a, t):
      if len(a) == 0:
          return False

      i = 0
      tSum = 0
      start = 0

      while i < len(a):
          if (tSum + a[i]) < t:
              tSum += a[i]
          elif (tSum + a[i]) == t:
              return True
          else:
              tSum += a[i]
              while tSum > t:
                  tSum -= a[start]
                  start += 1
              if tSum == t:
                  return True
              i += 1
       return False