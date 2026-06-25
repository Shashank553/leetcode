class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left< right:
            mid=(left+right)//2

            #make mid even
            if mid%2==1:
                mid=mid-1

            if nums[mid]==nums[mid+1]:
                left=mid+2
            else:
                right=mid

        return nums[left]

        