class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or stack.pop()!=pairs[ch]:
                    return False
        return not stack
        