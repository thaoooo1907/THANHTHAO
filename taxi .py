# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:46:13 2024

@author: Student
"""

km = float(input("nhap do dai quang duong da di (km): "))
tien = 3 * 13000 + 5 * 12000 + (km -8) * 10000 
if km > 1 :
    print ("tra 20k cho 1 km")
elif km  == 3 :
    print("so tien phai tra =", km * 13000 )
elif 4 <= km < 8 :
    print ("so tien phai tra =", km * 13000 + ((km -3 )*12000))
elif km > 8:
    print ("so tien phai tra =", (km * 13000 + ((km-3)*12000)+((km-8)*10000)))
    if tien > 100:
        print ("so tien phai tra sau cung=" , tien - (tien * 0.08))