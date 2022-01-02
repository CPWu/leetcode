class Solution(object):
    # # Time: O(N+MLogN+M), Space: O(N)
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: None Do not return anything, modify nums1 in-place instead.
    #     """
    #     for i in range(n):
    #         nums1[i+m] = nums2[i]
        
    #     return nums1.sort()

    #Time: O(N+M), Space: O(M)
    def merge(self, nums1, m, nums2, n):

        lastElement = n + m - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[lastElement] = nums1[m - 1]
                m -= 1
            else:
                nums1[lastElement] = nums2[n - 1]
                n -= 1
            lastElement -= 1
        
        while n > 0:
            nums1[lastElement] = nums2[n - 1]
            n -= 1
            lastElement -= 1

soln = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
soln.merge(nums1, m, nums2, n)
print(nums1)
