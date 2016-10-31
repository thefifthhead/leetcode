'''
 9. Palindrome Number

    Total Accepted: 160869
    Total Submissions: 478518
    Difficulty: Easy
    Contributors: Admin

Determine whether an integer is a palindrome. Do this without extra space.
'''
#beats 92.66% of python submissions. needs to be improved?
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        re = 1
        while x/re >= 10:
            re = re * 10
        while x > 0:
            lsd = x%10
            msd = x/re
            if lsd != msd:
                return False
            x = (x - msd * re)/10
            re = re/100
            if re == 0:
                return True
        return True

