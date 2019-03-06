# 打印200以内的素数即质数
import math
def isprime200():
	for i in range(2,201):
		for j in range(2,int(math.sqrt(i))+1):
			if i%j == 0:
				break
		else:
			print('{} '.format(i),end='')

