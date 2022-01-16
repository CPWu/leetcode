class Solution:
    def maximumSwap(self, num: int) -> int:
        # Time: O(N), Space: O(N)
        nums_list = list([int(c) for c in str(num)])
        last_index = {n:i for i,n in enumerate(nums_list)}

        
        for i, n in enumerate(nums_list):
            for d in range(9, n, -1):
                if d in last_index and last_index[d] > i:
                    nums_list[i], nums_list[last_index[d]] = nums_list[last_index[d]], nums_list[i]
                    return int(''.join([str(d) for d in nums_list]))
                
        return num