class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        


test = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = test.removeElement(nums, val)
print(k, nums)