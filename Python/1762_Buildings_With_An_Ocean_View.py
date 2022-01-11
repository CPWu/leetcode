class Solution(object):
    # Time: O(N), Space: O(1)
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """

        answer = []
        max_height = -1

        for current in reversed(range(len(heights))):
            if max_height < heights[current]:
                answer.append(current)

                max_height = heights[current]

        return reversed(answer)