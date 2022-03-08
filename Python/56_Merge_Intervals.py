class Solution:
    # Time: O(NlogN), Space: O(N)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Handles List of Lists with just one List.
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key = lambda interval: interval[0])
        result = [intervals[0]]
        
        # We can skip the first one as the first interval is in result.
        for start, end in intervals[1:]:
            # End value of the most recently added interval
            lastEnd = result[-1][1]
            
            if start <= lastEnd:
                # Take the most recently added interval to 
                # Take care of instances where the first interval end may be smaller/bigger than the second 
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])
        return result
                
