class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = '+'

        s += '+'  # Sentinel operator

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == ' ':
                continue

            else:
                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack.append(stack.pop() * num)

                elif sign == '/':
                    prev = stack.pop()

                    # Truncate toward zero
                    if prev < 0:
                        stack.append(-(-prev // num))
                    else:
                        stack.append(prev // num)

                sign = ch
                num = 0

        return sum(stack)