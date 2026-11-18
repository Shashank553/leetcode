class Solution:
    def minOperations(self, grid, x):
        nums = []

        for row in grid:
            for num in row:
                nums.append(num)

        for num in nums:
            if num % x != nums[0] % x:
                return -1

        nums.sort()
        target = nums[len(nums) // 2]

        ans = 0

        for num in nums:
            ans += abs(num - target) // x

        return ans