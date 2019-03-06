# isprime() 
# 参数为整数,要有异常处理,满足true 否则false
# 对正整数n，如果用2到根号n之间的所有整数去除，均无法整除，则n为质数
import math
def isprime():
		try:
			n = eval(input('输入一个自然数:'))
			if n <= 1 :
				return False
			for i in range(2,int (math.sqrt(n)) + 1):
				if n % i == 0:
					return False
			return True
		except:
			print('输入错误,亲输入一个自然数!')