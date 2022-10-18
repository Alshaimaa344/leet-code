# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:26:00 2022

@author: kcstore.com
"""

class Solution:
    def defangIPaddr(self, address):
        new_address=address.replace(".","[.]")
        return new_address