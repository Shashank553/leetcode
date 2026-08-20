class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count={}
        #step-1count the frequency of each character
        for ch in s:
            count[ch]=count.get(ch,0)+1
        #step-2: find firdt character  char with count=1
        for i in range(len(s)):
            if count[s[i]]==1:
                return i
        return -1