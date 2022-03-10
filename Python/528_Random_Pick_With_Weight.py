import random

class Solution:
    # Time: O(N), Space: O(N)
    def __init__(self, w: List[int]):
        # List to contain our cumulative sums
        self.cumulative_sum = []
        total = 0
        # Function to calculate cumulative sum
        for weight in w:
            total += weight
            self.cumulative_sum.append(total)
        # Store the total
        self.total = total 
        
    # # Time: O(N), Space: O(1)   
    # def pickIndex(self) -> int:
    #     pickedNumber = random.randint(1, self.total)
    #     for index, weight in enumerate(self.cumulative_sum):
    #         if pickedNumber <= weight:
    #             return index
    
    # Time: O(log N), Space: O(1)
    def pickIndex(self) -> int:
        
        pickedNumber = self.total * random.random()
        
        # Run a Binary Search
        low, high = 0, len(self.cumulative_sum)
        while low < high:
            middle = low + (high - low) // 2
            if pickedNumber > self.cumulative_sum[middle]:
                low = middle + 1
            else:
                high = middle
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()