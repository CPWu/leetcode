import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = []
        total = 0
        for weight in w:
            total += weight
            self.w.append(total)
        self.total = total

    def pickIndex(self):
        """
        :rtype: int
        """
        
        # run a binary search to find the target zone
        low, high = 0, len(self.w)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.w[mid]:
                low = mid + 1
            else:
                high = mid
        return low
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()