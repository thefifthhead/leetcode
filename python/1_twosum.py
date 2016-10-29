'''
1. Two Sum
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

    UPDATE (2016/2/13):
    The return format had been changed to zero-based indices. Please read the above updated description carefully.
'''
#Submission.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,x in enumerate(nums):
            if x in d:
                d[x].append(i)
            else:
                d[x] = [i]
        for v in nums:
            c = target - v
            if c in d:
                if c != v:
                    return [d[v][0], d[c][0]]
                elif c == v and len(d[c]) > 1 :
                    return [d[v][0], d[c][1]]
