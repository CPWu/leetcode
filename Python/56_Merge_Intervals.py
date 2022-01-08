class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Overlap is indicated when i1e > i2s 
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start > output[-1][1]:
                output.append([start, end])
            elif end > output[-1][1]:
                output[-1][1] = end
        return output


