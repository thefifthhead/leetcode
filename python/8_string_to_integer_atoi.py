'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        retval, sign, INT_MAX, INT_MIN = 0, 1, 2147483647,-2147483648
        chars = list(str.strip())
        if len(chars) == 0:
            return 0
        if chars[0] == '-':
            sign = -1
            chars = chars[1:]
        elif chars[0] == '+':
            sign = 1
            chars = chars[1:]
        for c in chars:
            a = ord(c)
            if a > 47 and a < 58:
                retval = retval * 10 + a - 48
            else :
                break
        out = sign * retval
        if (out > INT_MAX):
            return INT_MAX
        elif out <  INT_MIN:
            return INT_MIN
        return out
