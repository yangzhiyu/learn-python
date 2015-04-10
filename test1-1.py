#-*- coding:utf-8 -*-
#file: quadratic.py
import math
a, b, c = input(“请输入3个系数a,b,c: ”)
discRoot = math.sqrt(b*b – 4*a*c)
x1 = (-b + discRoot) / (2 * a)
x2 = (-b – discRoot) / (2 * a)
print “第1个解x1=”, x1
print “第2个解x1=”, x2
