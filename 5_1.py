# isnum()函数,输入字符串,if 整数/浮点数/复数,则返回 ture,否则false
def isNum(str):
	str = eval(str)
	if type(str) == type(3) or type(str) == type(3.0) or type(str) == type (1+2j):
		return True
	else:
		return False
isNum(input('亲输入:'))
