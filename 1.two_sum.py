class Solution:
    def twoSum(self, nums, target):
        num_map = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in num_map:
                return [num_map[diff], index]

            num_map[num] = index

solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))
