# 输入一行字符, 统计英文,数字,空格,和其他字符的个数
str = list(input('输入一行字符:'))
abc_counts=int_counts=kg_counts=other_count=0
for i in str :
	if i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
		abc_counts += 1
	elif i in '1234567890':
		int_counts += 1
	elif i in ' ':
		kg_counts += 1
	else :
		other_count += 1
print('英文:{}\n数字:{}\n空格:{}\n其他字符:{}\n'.format(abc_counts,int_counts,kg_counts,other_count))
