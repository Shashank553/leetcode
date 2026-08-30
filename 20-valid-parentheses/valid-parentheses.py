class Solution(object):
    def isValid(self, s):
        
        stack = []  # opening brackets ni store cheyadaniki

        pairs = {')':'(', ']':'[', '}':'{'}  # closing → opening pair

        for ch in s:

            if ch in pairs.values():
                stack.append(ch)  # opening bracket → PUSH chey

            else:
                # closing bracket → POP chesi match chey
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack  # stack empty unte → valid