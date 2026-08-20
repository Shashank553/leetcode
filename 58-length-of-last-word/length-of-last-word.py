class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word=s.split()
        x=word[-1]
        n=len(x)
        return n
        