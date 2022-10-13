# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:27:40 2022

@author: kcstore.com
"""
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):

            for j in range(i+1,len(nums)):
                 if(nums[i] + nums[j] == target):
                    return[i,j]