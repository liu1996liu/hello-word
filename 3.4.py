#--------回文数判断-----------
a = input("请输入数字:")
if a == a[::-1]:
	print('%a  is  yes' %a)
else:
	print('%a  is  no ' %a)
