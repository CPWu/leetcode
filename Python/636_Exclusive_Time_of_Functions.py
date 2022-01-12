class Solution(object):
    # Time: O(N), Space: O(N)
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        function_times = [0] * n
        stack = [] # the ids of the function calls
        prev_start_time = 0

        for log in logs:
            fid, type, timestamp = log.split(':')
            fid, timestamp = int(fid), int(timestamp)

            if type == 'start':
                if stack:
                    function_times[stack[-1]] += timestamp - prev_start_time
                stack.append(fid)
                prev_start_time = timestamp
            else:
                function_times[stack.pop()] += timestamp - prev_start_time + 1
                prev_start_time = timestamp + 1

        return function_times