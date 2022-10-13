# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:31:47 2022

@author: kcstore.com
"""

class Solution:
    def isPalindrome(self, n) :
        temp=n
        rev=0
        while(n>0):
            dig=n%10
            rev=rev*10+dig
            n=n//10
        if (temp==rev):
            return True
        else:
            return False