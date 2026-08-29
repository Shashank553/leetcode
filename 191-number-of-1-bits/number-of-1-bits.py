class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary=bin(n)[2:]
        count=0
        for bit in binary:
            if bit=='1':
                count=count+1
        return count