# 英文字符统计.
# a~z 字母频率进行分析,忽略大小写,降序
try:
	str = eval(input('亲输入一段字符串:'))
	# 大小写处理
	str = str.lower()
	# 处理特殊字符
	for str_i in '!~@#$%^&*()_+;[]\,./<>?:"{}|_=`':
		str = str.replace(str,'')
	# 处理字符
	str = list(str)
	# 统计
	counts = {}
	for word in str :
		if word in 'abcdefghijklmnopqrstuvwxyz':
			counts [i] = counts.get(word,0) + 1
	ls = list(counts.items())
	ls.sort(key=lambda x:x[1],reverse = Ture)
	for word in range (len(counts)):
		word,count = ls[i]
		print("{0:<10}{1:>5}".format(word,count))
except:
	print('输入错误,亲输入字符串')
