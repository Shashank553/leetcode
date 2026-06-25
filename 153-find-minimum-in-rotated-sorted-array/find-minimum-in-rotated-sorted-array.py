class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''nums.sort()
        return nums[0]'''
        #by using bunary search solution
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2

            if nums[mid]>nums[right]:
                #minimum is in the right half
                left=mid+1

            else:
                #minimum is at  mid or in the left half
                right=mid
        return nums[left]
        