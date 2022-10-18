# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:43:35 2022

@author: kcstore.com
"""

class Solution:
    def finalValueAfterOperations(self, operations):
        x=0
        for i in operations:
            if i=="++X" or i=="X++":
                
                x+=1
            else:
                
                x-=1
        return x