class Solution(object):

    # Time: O(NlogN), Space: O(N)
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        start  = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0

        startPointer, endPointer = 0,0

        while startPointer < len(intervals):
            if start[startPointer] < end[endPointer]:
                startPointer += 1
                count += 1
            else:
                endPointer += 1
                count -= 1
            res = max(res, count)

        return res