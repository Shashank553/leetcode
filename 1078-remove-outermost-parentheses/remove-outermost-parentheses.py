class Solution(object):
    def removeOuterParentheses(self, s):
        anss=[]
        count=0

        for ch in s:
            if ch =='(':
                if count>0:
                    anss.append(ch)
                count +=1
            else:
                count -=1
                if count > 0:
                    anss.append(ch)
        return ''.join(anss)
        