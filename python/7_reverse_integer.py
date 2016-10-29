'''
7. Reverse Integer

    Total Accepted: 180214
    Total Submissions: 760173
    Difficulty: Easy
    Contributors: Admin

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''
#beats 98.62% of python submissions.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign,r = 1,0
        if x < 0:
            x,sign = -1 * x,-1
        while x != 0:
            r = r * 10 + x % 10
            x = x/10
	#adding explicit overflow for 32 bit integer. python max int does not overflow. Input: 1534236469 expected output is 0.
        return 0 if r > 2147483647 else r * sign
