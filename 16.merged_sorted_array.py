class Solution:
    def merge(self, nums1, m, nums2, n):
        
        nums1[:] = sorted(nums1[:m] + nums2)


test = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
test.merge(nums1, m, nums2, n)
print(nums1)