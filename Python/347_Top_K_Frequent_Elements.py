from collections import Counter
class Solution(object):
    # Time: O(N), Space: O(N)
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # Build hash map by character: frequency
        # O(N)      
        count = Counter(nums)
        
        count = sorted(count, key=lambda x:count[x], reverse=True)
        
        return count[:k]

