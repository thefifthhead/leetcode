'''
2. Add Two Numbers

    Total Accepted: 201890
    Total Submissions: 790555
    Difficulty: Medium
    Contributors: Admin

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Beats 99.47% of python submissions.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c, h, t = 0, None, None
        while l1 or l2 or c !=0:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            d = d1 + d2 + c
            if d > 9:
                d = d - 10
                c = 1
            else:
                c = 0
            n = ListNode(d)
            if t:
                t.next = n
                t = t.next
            else:
                h = t = n
            l2 = l2.next if l2 else None
            l1 = l1.next if l1 else None
        return h

class ListNode(object):
    def __init__(self, x):
            self.val = x
            self.next = None

def printNode(n):
    while n:
        print n.val,'->',
        n = n.next

