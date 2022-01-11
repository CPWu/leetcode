class SparseVector:
#     # Time: O(N), Space: O(1)
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.array = nums
        

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec):
#         """
#         :type vec: 'SparseVector'
#         :rtype: int
#         """
#         result = 0
#         for num1, num2 in zip(self.array, vec.array):
#             result += num1 * num2
#         return result
        

# # Your SparseVector object will be instantiated and called as such:
# # v1 = SparseVector(nums1)
# # v2 = SparseVector(nums2)
# # ans = v1.dotProduct(v2)s

#     # Time: O(N), Space: O(1)
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nonzeros = {}
#         for i, n in enumerate(nums):
#             if n != 0:
#                 self.nonzeros[i] = n
        

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec):
#         """
#         :type vec: 'SparseVector'
#         :rtype: int
#         """
#         result = 0
#         # Iterate through each non-zero element in the sparse vector
#         # Updat the dot product if the corresponding index has a non-zero value in the other vector
#         for i, n in self.nonzeros.items():
#             if i in vec.nonzeros:
#                 result += n * vec.nonzeros[i]
#         return result
        

# # Your SparseVector object will be instantiated and called as such:
# # v1 = SparseVector(nums1)
# # v2 = SparseVector(nums2)
# # ans = v1.dotProduct(v2)

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)