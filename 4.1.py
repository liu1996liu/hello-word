# -*- coding: utf-8 -*-
# 第四章练习题,编程题1
# 输入一个年份,输出是否为闰年,能被4but不能被100整除,或者能被400整除
year = eval(input('输入一个年份:'))
if year%4 == 0 & year%100 != 0 | year%400 == 0:
	print(year ,'is 闰年')
else:
	print(year ,'not is 闰年')
	
	
