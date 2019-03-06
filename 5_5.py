# 求第n项 的斐波那契数列的数
import math
def Fibonacci_sequence(n):
	try:
		Fibonacci_sequence_an = (1/math.sqrt(5))*(((1+math.sqrt(5))/2)**n-(((1-math.sqrt(5))/2))**n)
		print(int(Fibonacci_sequence_an))
	except:
		print('输入一个整数!')
