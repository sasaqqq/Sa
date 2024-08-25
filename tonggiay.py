# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 07:57:53 2024

@author: Student
"""

gio=int(input("Nhập số giờ:"))
phut=int(input("Nhập số phút:"))
giay=int(input("Nhập số giây:"))
tong_giay = gio*3600 + phut*60 + giay
print("tổng số giây là:" , tong_giay)