# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:11:02 2024

@author: Student
"""

N=int(input("Nhập số nguyên dương N:"))
if 9 < N < 100:
    chuc = N // 10
    donvi = N % 10
print("Kết quả:" , chuc + donvi)