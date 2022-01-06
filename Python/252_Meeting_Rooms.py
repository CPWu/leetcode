class Solution(object):

    # Time: O(NlogN), Space: O(1)
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()

        for interval in range((intervals) - 1):
            if intervals[interval][1] > intervals[interval + 1][0]:
                return False
        return True