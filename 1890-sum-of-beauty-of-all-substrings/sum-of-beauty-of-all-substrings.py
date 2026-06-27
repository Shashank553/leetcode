class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        n=len(s)

        for i in range(n):
            freq=[0]*26

            for j in range(i,n):

                freq[ord(s[j])-ord('a')] +=1

                mx=0
                mn=float('inf')

                for f in freq:
                    if f>0:
                        mx=max(mx,f)
                        mn=min(mn,f)

                ans +=mx-mn
        return ans
        