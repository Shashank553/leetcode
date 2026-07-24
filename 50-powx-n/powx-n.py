#2.using  recursion method
class Solution(object):
    def myPow(self,x,n):
        #if n is negative
        if n<0:
            x=1/x
            n=-n


        #base case
        if n==0:
            return 1
        #recursive call
        half=self.myPow(x,n//2)

        #even power
        if n%2==0:
            return half*half

        #odd power
        else:
            return half*half*x