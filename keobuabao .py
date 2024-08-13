# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:56:27 2024

@author: Student
"""

import random
luachon = ["keo" , "bua", "bao"]
ngchoi = input ("lia chon (keo - bua - bao): ")
may = random.choice(luachon)
print (f"ban chon : {ngchoi}")
print (f"may chon: {may}")
if ngchoi == may:
    print ("hoa")
elif may == "bua" and ngchoi == "keo" or\
     may == "keo" and  ngchoi == "bao" or\
    may == "bao" and  ngchoi == "bua" or:
       print ("may thang") 
else: 
    print ("may thua")     