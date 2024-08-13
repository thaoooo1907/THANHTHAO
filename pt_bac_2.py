# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:01:25 2024

@author: Student
"""

a = float(input("nhap gia tri cua a (a<>0):"))
b = float(input("nhap gia tri cua b: "))
c = float (input("nhap gia tri cua c: "))
#a,b,c,= float(input("nhap gia tri a b c: "))
delta=b**2-4*a*c
if delta <0 :
    print ("phuong trinh vo nghiem")
    if delta == 0:
        print ("phuong trinh co nghiem kep x1=x2=, "-b/(2*a))
        if delta > 0:
            print ("phuong trinh co hai nghiem x1= ", (-b+ delta**0.5)/2*a,"x2 =", (-b-delta**0.5)/2*a)
    