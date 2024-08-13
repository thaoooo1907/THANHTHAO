# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:19:06 2024

@author: Student
"""
a = float(input("Nhập vào cạnh a: "))
b = float(input("Nhập vào cạnh b: "))
c = float(input("Nhập vào cạnh c: "))

x, y, z = sorted([a, b, c])

if a == b == c:
    print("Tam giác đều")
elif a == b or a == c or b == c:
    print("Tam giác cân")
elif x**2 + y**2 == z**2:
    print("Tam giác vuông")
elif x**2 + y**2 > z**2:
    print("Tam giác nhọn")
else:
    print("Tam giác tù")