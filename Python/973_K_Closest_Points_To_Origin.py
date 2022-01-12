import heapq

class Solution(object):
    
    # Time: O(N log k), Space: O(k)
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minHeap = []

        for x, y in points:
            dist = ( x ** 2) + (y ** 2)
            minHeap.append(([dist, x, y]))

        heapq.heapify(minHeap)
        result = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x,y])
            k -= 1

        return result

#     # Time: O(N log N), Space: O(N)
#     def kClosest(self, points, k):
#         """
#         :type points: List[List[int]]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         points.sort(key=self.squared_distance)
#         return points[:k]
    
#     def squared_distance(self, point):
#         return point[0] ** 2 + point[1] ** 2