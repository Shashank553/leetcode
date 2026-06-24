class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        x=[num**2 for num in nums]
        x.sort()
        return x
        