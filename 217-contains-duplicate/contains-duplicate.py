class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''return len(nums)!=len(set(nums))'''
        a={}
        for i in nums:
            if i in a:
                return True
            else:
                a[i]=1
        else:
            return False