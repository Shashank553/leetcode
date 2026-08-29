class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        x=n*(n+1)//2
        y=sum(nums)
        return x-y